"""
Nothing but a placeholder block
"""

from typing import override
from world.block import Block

class VoidBlock(Block):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__(pos)
        self.color = (255, 255, 255) # white

    @override
    def update(self):
        pass

    @override
    def draw(self, surface):
        pass
