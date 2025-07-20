"""
Most basic unit in world
"""

from typing import override
import pygame


class Block():
    _size = 16

    def __init__(self, pos: tuple[float, float]) -> None:
        # block position
        self.x = pos[0]
        self.y = pos[1]

        # neibouring blocks 
        self.neibouring_blocks: dict[str, Block | None] = {
            "up": None,
            "down": None,
            "left": None,
            "right": None
        }
        self.holder: BlockHolder

        # properies of the block
        self.properties: list[Property] = []

        # graphics of block
        self.base_color = (255, 0, 0)
        self.color = self.base_color

        # free flight properties
        self.velocity: tuple[float, float] = (0, 0)

        # must exceed size in either dimesion to move
        self.speed: tuple[float, float] = (0, 0)
        self.free = False

        # determines whether or not to draw
        self.to_draw = False

    def __eq__(self, other):
        if not isinstance(other, Block):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def set_color(self, color):
        self.color = color

    def set_holder(self, holder):
        self.holder = holder

    def enter_free_flight(self, velocity: tuple[float, float]): 
        self.velocity = velocity
        self.free = True

    def leave_free_flight(self, pos: tuple[float, float]):
        self.velocity = (0, 0)
        self.free = False

    def swap_blocks(self, block):
        """
        Swaps two blocks positions
        """
        temp = self.x
        self.x = block.x
        block.x = temp
        
        temp = self.y
        self.y = block.y
        block.y = temp

        # re assign neibouring blocks
        temp_neibours = {
            "up": self.neibouring_blocks["up"],
            "down": self.neibouring_blocks["down"],
            "left": self.neibouring_blocks["left"],
            "right": self.neibouring_blocks["right"]
        }

        # reassign holders
        temp_holder = self.holder
        self.holder.set_block(block)
        block.holder.set_block(self)

        # assign new self neibours
        for neibour in block.neibouring_blocks:
            if block.neibouring_blocks[neibour] == self:
                self.neibouring_blocks[neibour] = block
                continue
            self.neibouring_blocks[neibour] = block.neibouring_blocks[neibour]

        # assign new block neibours
        for neibour in temp_neibours:
            if temp_neibours[neibour] == block:
                block.neibouring_blocks[neibour] = self
                continue
            block.neibouring_blocks[neibour] = temp_neibours[neibour]

        # re evaluate neibours beleif in their neibour
        if self.neibouring_blocks["up"] is not None: 
            self.neibouring_blocks["up"].neibouring_blocks["down"] = self
        if self.neibouring_blocks["down"] is not None: 
            self.neibouring_blocks["down"].neibouring_blocks["up"] = self
        if self.neibouring_blocks["left"] is not None: 
            self.neibouring_blocks["left"].neibouring_blocks["right"] = self
        if self.neibouring_blocks["right"] is not None: 
            self.neibouring_blocks["right"].neibouring_blocks["left"] = self

        if block.neibouring_blocks["up"] is not None:
            block.neibouring_blocks["up"].neibouring_blocks["down"] = block
        if block.neibouring_blocks["down"] is not None:
            block.neibouring_blocks["down"].neibouring_blocks["up"] = block
        if block.neibouring_blocks["left"] is not None:
            block.neibouring_blocks["left"].neibouring_blocks["right"] = block
        if block.neibouring_blocks["right"] is not None:
            block.neibouring_blocks["right"].neibouring_blocks["left"] = block
       
    def move(self):
        """
        Updates the blocks speed and if nessicary moves and
        swaps the blocks positions
        """

        # increase speed
        self.speed = (self.speed[0] + self.velocity[0], 
                      self.speed[1] + self.velocity[1])

        if self.speed[0] >= Block._size:
            self.speed = (self.speed[0] - Block._size, self.speed[1])
            self.swap_blocks(self.neibouring_blocks["right"])
        elif self.speed[0] <= -Block._size:
            self.speed = (self.speed[0] + Block._size, self.speed[1])
            self.swap_blocks(self.neibouring_blocks["left"])

        if self.speed[1] >= Block._size:
            self.speed = (self.speed[0], self.speed[1] - Block._size)
            self.swap_blocks(self.neibouring_blocks["down"])
        elif self.speed[1] <= -Block._size:
            self.speed = (self.speed[0], self.speed[1] + Block._size)
            self.swap_blocks(self.neibouring_blocks["up"])
        
    def get_index(self):
        return (int(self.x / Block._size), int(self.y / Block._size))

    def check_property(self, property) -> bool:
        for p in self.properties:
            if isinstance(p, property):
                return True
        return False

    def set_to_draw(self, to_draw: bool):
        self.to_draw = to_draw
    
    def draw(self, surface: pygame.surface.Surface):
        if not self.to_draw:
            return
        # draw block
        pygame.draw.rect(surface, self.color, 
                         (self.x, self.y, Block._size, Block._size)) 

    def update(self):
        # update all properties
        for property in self.properties:
            property.update(self)

        # update any movement
        if self.free:
            self.move()

"""
A abstract position that hold one block
"""
class BlockHolder():
    def __init__(self) -> None:
        self.block: Block | None = None

    def set_block(self, block: Block):
        self.block = block
        self.block.set_holder(self) 

    def draw(self, surface: pygame.surface.Surface):
        if self.block is None:
            return
        self.block.draw(surface)

    def update(self):
        if self.block is None:
            return
        self.block.update()

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
        self.gravity: int = 3

    @override     
    def update(self, block: Block):
        super().update(block)
        # check if a solid block exists below
        if block.neibouring_blocks["down"] is None or block.neibouring_blocks["down"].check_property(SolidProperty) is False:
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

