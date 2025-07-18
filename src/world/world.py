"""
A world grid of blocks
should store block positions in a matrix
"""

import pygame
from world.block import Block, SolidProperty

class World():
    def __init__(self, size: tuple[int, int]) -> None:
        # create empty world
        self.static_blocks = [[Block((x * Block._size, y * Block._size)) 
                                        for x in range(size[0])] 
                                        for y in range(size[1])]

    def draw(self, surface):
        for row in self.static_blocks:
            for block in row:
                block.draw(surface)

    def update(self):
        for row in self.static_blocks:
            for block in row:
                block.update()

    def update_blocks_for_block(self, block):
        """
        update all blocks that are affected by the free block
        """
        pass

from world.property import Property
