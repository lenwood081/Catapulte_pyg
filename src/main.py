"""
Main entry point for game
Contains the main game loop
"""

import pygame
from screens.screen import Screen
from screens.screenFactory import Screen_Factory
import time
import sys

pygame.init()

screen: Screen | None = Screen_Factory.get_instance().main_menu_screen()

# delta time
clock = pygame.time.Clock()
FRAMERATE = 60
last_time = time.time()

running = True
while running:
    dt = time.time() - last_time
    dt *= FRAMERATE
    last_time = time.time()

    # get inputs
    events = pygame.event.get()
    keys_pressed = pygame.key.get_pressed()
    mouse_pressed = pygame.mouse.get_pressed()

    # handle forced exit event
    for event in events:
        if event.type == pygame.QUIT:
            # clean exit
            pygame.quit()
            sys.exit()

    # get events and pass to screen
    screen = screen.run(dt, (events, keys_pressed, mouse_pressed))

    # check if screen exists
    if screen is None:
        running = False

    pygame.display.update()

    # framerate 
    clock.tick(FRAMERATE)

