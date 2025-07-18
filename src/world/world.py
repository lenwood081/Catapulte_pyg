"""
A world grid of blocks
should store block positions in a matrix
"""

from world.block import Block
from world.blockTypes.obsidian import ObsidianBlock 

class World():
    def __init__(self, size: tuple[int, int]) -> None:
        # create empty world
        self.blocks = [[ObsidianBlock((0, 0)), ObsidianBlock((Block._size, 0))],
                        [ObsidianBlock((0, Block._size))]]


    def draw(self, surface):
        for row in self.blocks:
            for block in row:
                if block is None:
                    continue
                block.draw(surface)

    def update(self):
        for row in self.blocks:
            for block in row:
                if block is None:
                    continue
                block.update()

