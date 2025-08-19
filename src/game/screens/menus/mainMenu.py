# import screens
from typing import override
from screens.screen import Screen
from pygame.locals import K_q, K_ESCAPE, K_RETURN
from menu.button import Button

class MainMenu(Screen):
    def __init__(self, window):
        super().__init__(window)

        self.buttons: list[Button] = []

        self.buttons.append(Button())

    @override
    def draw(self):
        # create background
        self.window.fill((0, 255, 0)) 
        
        # draw buttons
        for button in self.buttons:
            button.draw(self.window)

    @override 
    def run(self, dt: float, events):
        super().run(dt, events)

        # check for exiting keypresses
        if events[1][K_q]: 
            return None
        
        #if events[1][K_RETURN]: 
        #    from screens.screenFactory import Screen_Factory
        #    return Screen_Factory.get_instance().main_game_screen()
        
        self.draw()
        return self


    
