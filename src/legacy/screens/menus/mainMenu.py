# import screens
from typing import override
from screens.screen import Screen
from pygame.locals import K_q, K_ESCAPE, K_RETURN

class MainMenu(Screen):
    def __init__(self, window):
        super().__init__(window)

    @override
    def draw(self):
        # create background
        self.window.fill((0, 255, 0)) 

    @override 
    def run(self, dt: float, events):
        # check for exiting keypresses
        if events[1][K_q]: 
            return None
        
        if events[1][K_RETURN]: 
            from screens.screenFactory import Screen_Factory
            return Screen_Factory.get_instance().main_game_screen()
        
        self.draw()
        return self


    
