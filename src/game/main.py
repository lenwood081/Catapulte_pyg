"""
Main entry point for game
Contains the main game loop
"""

import pygame
from screens.screen import Screen
from screens.screenFactory import Screen_Factory
import time
import sys

class Main:
    def __init__(self) -> None:
        self.FRAMERATE = 20

    def start_game(self):
        pygame.init()

        screen: Screen | None = Screen_Factory.get_instance().main_menu_screen()

# delta time
        clock = pygame.time.Clock()
        last_time = time.time()

        running = True
        while running:
            dt = time.time() - last_time
            dt *= self.FRAMERATE
            last_time = time.time()
            # print(dt) # DEBUG

            # get inputs
            events = pygame.event.get()
            keys_pressed = pygame.key.get_pressed()
            mouse_pressed = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # handle forced exit event
            for event in events:
                if event.type == pygame.QUIT:
                    # clean exit
                    pygame.quit()
                    sys.exit()

            # get events and pass to screen
            screen = screen.run(dt, (events, keys_pressed, mouse_pressed, (mouse_x, mouse_y)))

            # check if screen exists
            if screen is None:
                running = False

            pygame.display.update()

            # framerate 
            clock.tick(self.FRAMERATE)

main = Main()
main.start_game()
