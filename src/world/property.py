"""
A property of a block
"""

from typing import override
from world.block import Block

class Property:
    def __init__(self) -> None:
        # spread value (how many turn to spread)
        self.spread: int | None = None

    def set_spread(self, spread: int):
        self.spread = spread
    
    def update(self, block: Block):
        pass

class SolidProperty(Property):
    def __init__(self) -> None:
        super().__init__()

class GravityProperty(Property):
    def __init__(self) -> None:
        super().__init__()
        self.gravity: int = 1
        
    @override
    def update(self, block: Block):
        # check if a solid block exists below
        pass        

class FireProperty(Property):
    def __init__(self) -> None:
        super().__init__()

