"""
Most basic unit in world
"""

from typing import override


class Block():
    _size = 32

    def __init__(self, pos: tuple[float, float]) -> None:
        # block position
        self.x = pos[0]
        self.y = pos[1]

        # neibouring blocks
        self.up = None
        self.down = None
        self.left = None
        self.right = None

        # properies of the block
        self.properties: list[Property] = []

        # graphics of block
        self.base_color = (255, 0, 0)
        self.color = self.base_color

        # free flight properties
        self.velocity: tuple[float, float] = (0, 0)
        self.free = False

    def set_color(self, color):
        self.color = color

    def enter_free_flight(self, velocity: tuple[float, float]): 
        self.velocity = velocity
        self.free = True

    def leave_free_flight(self, pos: tuple[float, float]):
        self.velocity = (0, 0)
        self.free = False
        self.pos = pos

    def set_neibours(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def get_index(self):
        return (int(self.x / Block._size), int(self.y / Block._size))

    def check_property(self, property) -> bool:
        for p in self.properties:
            if isinstance(p, property):
                return True
        return False
    
    def draw(self, surface):
        pass

    def update(self):
        # update all properties
        for property in self.properties:
            property.update(self)

        # fly
        if self.free:
            self.x += self.velocity[0]
            self.y += self.velocity[1]

"""
A property of a block
"""

class Property:
    def __init__(self) -> None:
        # spread value (how many turns to spread) (-1 = no spread)
        self.spread: int = -1
        self.spread_count: int = 0

    def set_spread(self, spread: int):
        self.spread = spread
    
    def update(self, block: Block):
        # increment spread count
        if (self.spread_count < self.spread):
            self.spread_count += 1

class SolidProperty(Property):
    def __init__(self) -> None:
        super().__init__()

class GravityProperty(Property):
    def __init__(self) -> None:
        super().__init__()
        self.gravity: int = 1

    @override     
    def update(self, block: Block):
        super().update(block)
        # check if a solid block exists below
        if not block.down or not block.down.check_property(SolidProperty):
            block.enter_free_flight((0, self.gravity))

class FireProperty(Property):
    def __init__(self) -> None:
        super().__init__()

    @override
    def update(self, block: Block):
        super().update(block)
        # spread fire
        if self.spread_count == self.spread:
            # reset spread count
            self.spread_count = 0

