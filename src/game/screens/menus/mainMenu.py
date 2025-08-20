import pygame
from libManager import LibManager
from typing import override
from screens.game.mainGame import MainGame
from screens.game.serverGame import ServerGame
from screens.game.clientGame import ClientGame
from screens.screen import Screen
from pygame.locals import K_q, K_ESCAPE, K_RETURN
from menu.button import ScreenChangeButton, Button

class MainMenu(Screen):
    def __init__(self, window):
        super().__init__(window)

        self.buttons: dict[str, Button] = {}

        self.buttons["serverGame"] = ScreenChangeButton(self, ServerGame)
        self.buttons["mainGame"] = ScreenChangeButton(self, MainGame)
        self.buttons["clientGame"] = ScreenChangeButton(self, ClientGame)

        self.buttons["serverGame"].set_dimensions(x=100, y=100)
        self.buttons["mainGame"].set_dimensions(x=100, y=400)
        self.buttons["clientGame"].set_dimensions(x=100, y=200)

        button_surface = LibManager.get_instance().get_button_surface("Local.png")
        self.buttons["mainGame"].set_image(button_surface)
        self.buttons["mainGame"].scale_image(3)

        button_surface = LibManager.get_instance().get_button_surface("Host.png")
        self.buttons["serverGame"].set_image(button_surface)
        self.buttons["serverGame"].scale_image(3)

        button_surface = LibManager.get_instance().get_button_surface("Join.png")
        self.buttons["clientGame"].set_image(button_surface)
        self.buttons["clientGame"].scale_image(3)


    @override
    def draw(self):
        # create background
        self.window.fill((0, 255, 0)) 
        
        # draw buttons
        for button in self.buttons.values():
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
        return self.queued_screen


    
