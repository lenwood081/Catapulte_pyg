# import screens
from typing import override
from screens.screen import Screen
from pygame.locals import K_ESCAPE
from world.worldTypes.testWorld import TestWorld
from camera.camera import Camera

class MainGame(Screen):
    def __init__(self, window):
        super().__init__(window)

        self.world = TestWorld((400, 400))
        self.camera = Camera(400, 400)

    @override
    def draw(self):
        # create background
        self.window.fill((255, 255, 0)) 
        
        # draw world
        self.world.draw(self.camera)
        self.camera.draw(self.window)

    @override 
    def run(self, dt: float, events):
        # check for exiting keypresses
        if events[1][K_ESCAPE]:
            from screens.screenFactory import Screen_Factory
            return Screen_Factory.get_instance().main_menu_screen()
        
        self.draw()
        return self


 
