from typing import override
from world.world import World

"""
World that simply reflects what is received via update pusher
Does not predicte
"""

class ReflectionWorld(World):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size)

        # list of blocks in the world for easy lookup
        # update this list based on update pusher
        # changes in position need to be reflected by changing the block hodler responsible
        # unique ID determined by block ID
        self.blocks = []

    def assign_block(self, block):
        # use position of block to assing it to a approprite block holder
        x, y = block.get_index()
        print(x, y)
        self.world[x][y].set_block(block)

    @override 
    def update(self, dt: float):
        # update blocks in world based on update pusher
        pass


