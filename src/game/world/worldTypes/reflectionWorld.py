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

    @override 
    def update(self, dt: float):

        # update blocks in world based on update pusher

        pass
