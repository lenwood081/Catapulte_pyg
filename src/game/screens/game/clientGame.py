from client.tcpClient import TCPClient
from client.UpdateReceiver import UpdateReceiver
from camera.cameras.devCamera import DevCamera
from world.world import World
from world.worldTypes.reflectionWorld import ReflectionWorld
from screens.screen import Screen
from typing import override
from camera.cameras.devCamera import DevCamera
from pygame.locals import K_ESCAPE

"""
Client Game
reflects the packets recived from the server
predicts next updates
compares differences and backtracks if nessicary
"""

class ClientGame(Screen):
    def __init__(self, window):
        super().__init__(window)

        # world and camera placeholders
        self.world: World 
        self.camera: DevCamera 

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
        if self.world:
            self.world.draw(self.camera)
        if self.camera:
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
        while frame:
            # print(frame) # DEBUG

            # parse frame data to UpdateReceiver
            UpdateReceiver.get_instance().upload_frame(frame)

            if UpdateReceiver.get_instance().get_frame_number() == 0:
                self.world, self.camera = UpdateReceiver.get_instance().unpack_start_data(ReflectionWorld, DevCamera)

            frame = self.client.get_new_frame()
        
        if UpdateReceiver.get_instance().get_frame_number() == 0:
            return self 
        
        self.update(dt)
        self.draw()
        return self


 

