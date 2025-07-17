# import screens
from typing import override
from screens.screen import Screen
from pygame.locals import K_ESCAPE

class MainGame(Screen):
    def __init__(self, window):
        super().__init__(window)

    @override
    def draw(self):
        # create background
        self.window.fill((255, 255, 0)) 

    @override 
    def run(self, dt: float, events):
        # check for exiting keypresses
        if events[1][K_ESCAPE]:
            from screens.screenFactory import Screen_Factory
            return Screen_Factory.get_instance().main_menu_screen()
        
        self.draw()
        return self


 
