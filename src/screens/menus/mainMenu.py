# import screens
from typing import override
from screens.screen import Screen
import pygame
from pygame.locals import K_q, K_ESCAPE

class MainMenu(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)

    @override
    def draw(self):
        # create background
        self.screen.fill((0, 255, 0)) 

    @override 
    def run(self, dt: float, events):
        # check for exiting keypresses
        if events[1][K_q] or events[1][K_ESCAPE]:
            return None
        
        self.draw()
        return self


    
