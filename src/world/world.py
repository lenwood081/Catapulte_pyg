"""
A world grid of blocks
should store block positions in a matrix
"""

import pygame
from camera.camera import Camera
from world.block import Block, BlockHolder
from world.blockTypes.obsidian import ObsidianBlock
from world.blockTypes.void import VoidBlock 

class World():
    def __init__(self, size: tuple[int, int]) -> None:
        # position in pixel
        self.x_p, self.y_p = size

        # index position in world
        self.x = self.x_p//Block._size
        self.y = self.y_p//Block._size

        # create empty world
        self.world = [[BlockHolder() for i in range(self.x)] for j in range(self.y)]
        self.set_neibours()

        self.surface = pygame.surface.Surface((self.x_p, self.y_p))

    def set_neibours(self):
        """
        Assign neibours to all blocks in world
        """
        for i in range(self.x):
            for j in range(self.y):
                # up
                if (j-1) >= 0:
                    self.world[i][j].neibours["up"] = self.world[i][j-1]
                else:
                    self.world[i][j].neibours["up"] = None

                # down
                if (j+1) < self.y:
                    self.world[i][j].neibours["down"] = self.world[i][j+1]
                else:
                    self.world[i][j].neibours["down"] = None

                # left
                if (i-1) >= 0:
                    self.world[i][j].neibours["left"] = self.world[i-1][j]
                else:
                    self.world[i][j].neibours["left"] = None

                # right
                if (i+1) < self.x:
                    self.world[i][j].neibours["right"] = self.world[i+1][j]
                else:
                    self.world[i][j].neibours["right"] = None


    def void_fill(self):
        """
        Fill all blockholders with void block
        """
        for i in range(self.x):
            for j in range(self.y):
                self.world[i][j].set_block(VoidBlock((i*Block._size, 
                                                    j*Block._size)))

    def obsidian_border(self):
        """
        create an obsidian border
        """
        for i in range(self.x):
            self.world[i][0].set_block(ObsidianBlock((i*Block._size, 0)))
            self.world[i][self.y-1].set_block(ObsidianBlock((i*Block._size, 
                                                (self.y-1)*Block._size)))

        for j in range(self.y):
            self.world[0][j].set_block(ObsidianBlock((0, j*Block._size)))
            self.world[self.x-1][j].set_block(ObsidianBlock((
                                 (self.x-1)*Block._size, j*Block._size)))

    def draw(self, camera: Camera):
        self.surface.fill((200, 200, 200))
        for row in self.world:
            for block in row:
                block.draw(self.surface)
        
        # draw to camera
        camera.draw_surface(self.surface)

    def update(self):
        for row in self.world:
            for block in row:
                block.update()

