"""
A 'Camera'
is esentually just a surface that things get
blit reletive too
"""

import pygame

class Camera:
    def __init__(self, width, height):
        self.surface = pygame.surface.Surface((width, height))
        self.surface.fill((255, 255, 255))
        self.width = width
        self.height = height

        # relative position to the world
        self.x = 0
        self.y = 0

    def draw(self, surface):
        surface.blit(self.surface, (0, 0)) 

    def draw_surface(self, surface: pygame.surface.Surface) -> None:
        self.surface.blit(surface, (self.x, self.y))
