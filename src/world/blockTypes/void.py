"""
Nothing but a placeholder block
"""

from typing import override
from world.block import Block, GasProperty

class VoidBlock(Block):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__(pos)
        self.properties.append(GasProperty())
        self.properties[0].set_spread(-1)


    @override
    def update(self):
        pass

    @override
    def draw(self, surface):
        # clear
        pass
