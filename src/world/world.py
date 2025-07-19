"""
A world grid of blocks
should store block positions in a matrix
"""

import pygame
from camera.camera import Camera
from world.block import Block
from world.blockTypes.void import VoidBlock 
from world.blockTypes.obsidian import ObsidianBlock

class World():
    def __init__(self, size: tuple[int, int]) -> None:
        self.x_p, self.y_p = size
        self.x = self.x_p//Block._size
        self.y = self.y_p//Block._size

        # create empty world
        self.blocks = [[Block((i*Block._size, j*Block._size)) for i in range(self.x)] for j in range(self.y)]


        self.surface = pygame.surface.Surface((self.x_p, self.y_p))

    def obsidian_border(self):
        """
        create an obsidian border
        """
        for i in range(self.x):
            self.blocks[i][0] = ObsidianBlock((i*Block._size, 0))
            self.blocks[i][self.y-1] = ObsidianBlock((i*Block._size, (self.y-1)*Block._size))

        for j in range(self.y):
            self.blocks[0][j] = ObsidianBlock((0, j*Block._size))
            self.blocks[self.x-1][j] = ObsidianBlock(((self.x-1)*Block._size, j*Block._size))

    def draw(self, camera: Camera):
        self.surface.fill((200, 200, 200))
        for row in self.blocks:
            for block in row:
                if block is None:
                    continue
                block.draw(self.surface)
        
        # draw to camera
        camera.draw_surface(self.surface)

    def update(self):
        for row in self.blocks:
            for block in row:
                if block is None:
                    continue
                block.update()

