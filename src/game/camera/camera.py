"""
A 'Camera'
is esentually just a surface that things get
blit reletive too
"""

import pygame

class Camera:
    def __init__(self, dimensions: tuple[float, float]):
        self.surface = pygame.surface.Surface(dimensions)
        self.surface.fill((255, 255, 255))
        self.width, self.height = dimensions

        # relative position to the world
        self.x = 0
        self.y = 0

    def draw(self, surface):
        surface.blit(self.surface, (0, 0)) 

    def draw_surface(self, surface: pygame.surface.Surface) -> None:
        self.surface.blit(surface, (self.x, self.y))
