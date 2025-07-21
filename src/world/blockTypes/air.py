"""
Air gas
"""

from world.block import Block, GasProperty

class AirBlock(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.base_color = (119, 172, 199)
        self.color_vary(10, 10, 10)
        self.properties.append(GasProperty())
        self.properties[-1].set_spread(10)
        self.set_to_draw(True)
