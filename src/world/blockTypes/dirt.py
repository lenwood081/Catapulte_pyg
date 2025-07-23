from world.block import Block, SolidProperty, GravityProperty


class DirtBlock(Block):
    def __init__(self, pos: tuple[int, int]):
        super().__init__(pos)
        self.set_color((128, 64, 0))
        self.properties.append(SolidProperty())
        self.properties.append(GravityProperty())
        self.set_to_draw(True)
