"""
A simple obsidian surrounded world for testing
during development
"""

from world.blockTypes.air import AirBlock
from world.world import World
from world.block import Block
from world.blockTypes.dirt import DirtBlock

class TestWorld(World):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size)
        #self.void_fill()
        self.void_fill()
        self.obsidian_border()

        self.world[5][1].set_block(DirtBlock((5*Block._size, 1*Block._size)))
        self.world[5][5].set_block(DirtBlock((5*Block._size, 5*Block._size)))
        self.world[10][10].set_block(AirBlock((10*Block._size, 10*Block._size)))
        
