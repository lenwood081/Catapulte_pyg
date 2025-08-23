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
        self.base_color = (100, 100, 100)
        self.color_vary(10, 10, 10)
        self.set_to_draw(True)

