"""
A simple obsidian surrounded world for testing
during development
"""

from world.world import World
from world.block import Block
from world.blockTypes.air import AirBlock

class TestWorld(World):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size)
        self.void_fill()
        self.obsidian_border()

        # create a air block
        self.world[5][5].set_block(AirBlock((5*Block._size, 5*Block._size)))
        self.world[20][20].set_block(AirBlock((20*Block._size, 20*Block._size)))

