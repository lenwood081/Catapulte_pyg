from screens.screen import Screen
from server.updatePusher import UpdatePusher
import threading
from typing import override
from camera.cameras.devCamera import DevCamera
from world.worldTypes.testWorld import TestWorld
from pygame.locals import K_ESCAPE
from observers.observer import ObserverFactory
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

        self.server = TCPServer()
        self.server_thread = threading.Thread(target=self.server.start)
        self.server_thread.start()
        UpdatePusher.get_instance().activate()
    
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
        
        # only run if there is a connection
        if not self.server.clients_connected():
            return self

        UpdatePusher.get_instance().increase_frame_number()

        # check for exiting keypresses
        if events[1][K_ESCAPE]:
            self.server.end_connection()

            from screens.screenFactory import Screen_Factory
            from screens.menus.mainMenu import MainMenu
            return Screen_Factory.get_instance().get_screen(MainMenu)

        self.update(dt)
        # push updates to clients
        self.server.add_frame(UpdatePusher.get_instance().get_update())

        self.draw()
        print(dt) # DEBUG

        return self.queued_screen


 


