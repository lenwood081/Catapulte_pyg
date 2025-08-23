from client.tcpClient import TCPClient
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
        self.client.start_connection_thread()
    
    @override
    def update(self, dt: float) -> None:
        super().update(dt)

        # update world
        # self.world.update(dt)

    @override
    def draw(self):
        # create background
        self.window.fill((255, 255, 0)) 
        
        # draw world
        # self.world.draw(self.camera)
        self.camera.draw(self.window)

    @override 
    def run(self, dt: float, events):
        super().run(dt, events)

        # check for exiting keypresses
        if events[1][K_ESCAPE]:
            self.client.stop_connection()

            from screens.screenFactory import Screen_Factory
            from screens.menus.mainMenu import MainMenu
            return Screen_Factory.get_instance().get_screen(MainMenu)

        # only run if there is a connection
        if not self.client.get_active_connection():
            return self

        # get frame data from tcp client
        frame = self.client.get_new_frame()
        if frame:
            print(frame)
            # parse frame data to world
        
        self.update(dt)

        self.draw()
        return self


 

