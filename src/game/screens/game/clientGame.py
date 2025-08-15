from tcpClient import TCPClient
import threading
from screens.screen import Screen
from typing import override
from camera.cameras.devCamera import DevCamera
from pygame.locals import K_ESCAPE
from observers.observer import ObserverFactory

"""
Client Game
reflects the packets recived from the server
predicts next updates
compares differences and backtracks if nessicary
"""

class ClientGame(Screen):
    def __init__(self, window):
        super().__init__(window)

        # special client world
        self.world = None
        self.camera = DevCamera(800, 600)

        self.client = TCPClient()
        self.client_thread = threading.Thread(target=self.client.start)
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
        # only run if there is a connection
        if not self.server.clients_connected():
            return self

        UpdatePusher.get_instance().increase_frame_number()

        # check for exiting keypresses
        if events[1][K_ESCAPE]:
            from screens.screenFactory import Screen_Factory
            self.server.end_connection()
            return Screen_Factory.get_instance().main_menu_screen()

        # inform observers
        ObserverFactory.get_instance().get_arrorK().notify(events[1])
        ObserverFactory.get_instance().get_mouse_left_click_pos().notify((events[2], events[3]))
        
        self.update(dt)
        # push updates to clients
        self.server.add_frame(UpdatePusher.get_instance().get_update())

        self.draw()
        print(dt) # DEBUG
        return self


 

