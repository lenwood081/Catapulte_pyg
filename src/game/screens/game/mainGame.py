# import screens
from typing import override
from screens.screen import Screen
from pygame.locals import K_ESCAPE
from world.worldTypes.testWorld import TestWorld
from camera.cameras.devCamera import DevCamera
from observers.observer import ObserverFactory

class MainGame(Screen):
    def __init__(self, window):
        super().__init__(window)

        self.world = TestWorld((800, 600))
        self.camera = DevCamera((800, 600))

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
        # check for exiting keypresses
        if events[1][K_ESCAPE]:
            from screens.menus.mainMenu import MainMenu
            from screens.screenFactory import Screen_Factory
            return Screen_Factory.get_instance().get_screen(MainMenu)

        self.update(dt)
        self.draw()
        return self.queued_screen


 
