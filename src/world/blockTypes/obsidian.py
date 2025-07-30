"""
Block that isnt affected by gravity, fire or any thing like that
it is solid
it cannot be moved
"""

from world.block import Block, SolidProperty

class ObsidianBlock(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.base_color = (0, 0, 0)
        self.set_color((0, 0, 0))
        self.properties.append(SolidProperty())
        self.set_to_draw(True)

