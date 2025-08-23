from screens.screen import Screen
from server.updatePusher import UpdatePusher
import threading
from typing import override
from camera.cameras.devCamera import DevCamera
from world.worldTypes.testWorld import TestWorld
from pygame.locals import K_ESCAPE
from server.tcpServer import TCPServer

"""
Server Game, authorative as to the game state
recives infromation from clients
tcp connections to clients
sends updated blocks at each tick
"""

class ServerGame(Screen):
    def __init__(self, window):
        super().__init__(window)

        self.world = TestWorld((800, 600))
        self.camera = DevCamera(800, 600)

        # start server thread here, not using method
        # as the diagnostic does not pick it up
        self.server = TCPServer()
        self.server_thread = threading.Thread(target=self.server.start)
        self.server_thread.start()
        UpdatePusher.get_instance().activate()

        self.server_active = True

    def complile_start_data(self):
        # get state of starting blocks, world size, etc

        # blocks
        blocks = self.world.compile_start_data()

        from world.block import Block

        state = {
            "block_size": Block._size,
            "world_size": (self.world.x, self.world.y),
            "camera_size": (self.camera.x, self.camera.y),
            "blocks": blocks,
        }
        
        UpdatePusher.get_instance().add_update(state)


    def start_server_thread(self):
        self.server = TCPServer()
        self.server_thread = threading.Thread(target=self.server.start)
        self.server_thread.start()
        UpdatePusher.get_instance().activate()
        self.server_active = True
    
    @override
    def update(self, dt: float) -> None:
        super().update(dt)

        # update world
        self.world.update(dt)

    @override
    def draw(self):
        # create background
        self.window.fill((255, 255, 0)) 
        
        # draw world
        self.world.draw(self.camera)
        self.camera.draw(self.window)

    @override 
    def run(self, dt: float, events):
        super().run(dt, events)

        # start server if not already started
        if not self.server_active:
            self.start_server_thread()

        # check for exiting keypresses
        if events[1][K_ESCAPE]:
            self.server.end_server()
            self.server_active = False
            UpdatePusher.get_instance().deactivate()

            from screens.screenFactory import Screen_Factory
            from screens.menus.mainMenu import MainMenu
            return Screen_Factory.get_instance().get_screen(MainMenu)
        
        # only run if there is a connection
        if not self.server.clients_connected():
            return self

        # if first frame, send starting data
        if UpdatePusher.get_instance().get_frame_number() == 0:
            self.complile_start_data()
        else:
            self.update(dt)
            self.draw()

        # push updates to clients
        self.server.add_frame(UpdatePusher.get_instance().get_update())
        UpdatePusher.get_instance().increase_frame_number()
        return self.queued_screen


 


