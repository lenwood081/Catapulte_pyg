"""
Most basic unit in world
"""

from typing import override
import pygame


class Block():
    _size = 16
    _block_count = 0

    def __init__(self, pos: tuple[float, float]) -> None:
        self.__class__._block_count += 1
        # block position
        self.x = pos[0]
        self.y = pos[1]

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

    def simple_varience(self, low: int, high: int) -> int:
        difference = (high - low)
        value = low + self.__class__._block_count % difference
        print(value)
        return value

    def color_vary(self, var_r: int, var_g: int, var_b: int) -> None:
        self.base_color = (self.simple_varience(self.base_color[0] - var_r, self.base_color[0] + var_r),
                      self.simple_varience(self.base_color[1] - var_g, self.base_color[1] + var_g),
                      self.simple_varience(self.base_color[2] - var_b, self.base_color[2] + var_b))

        if self.base_color[0] < 0:
            self.base_color = (0, self.base_color[1], self.base_color[2])
        if self.base_color[1] < 0:
            self.base_color = (self.base_color[0], 0, self.base_color[2])
        if self.base_color[2] < 0:
            self.base_color = (self.base_color[0], self.base_color[1], 0)

        if self.base_color[0] > 255:
            self.base_color = (255, self.base_color[1], self.base_color[2])
        if self.base_color[1] > 255:
            self.base_color = (self.base_color[0], 255, self.base_color[2])
        if self.base_color[2] > 255:
            self.base_color = (self.base_color[0], self.base_color[1], 255)

        self.color = self.base_color

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

    def dupulicate(self, block):
        dupulicate = self.__class__((block.x, block.y))
            
        # change holder
        dupulicate.holder = block.holder
        dupulicate.holder.set_block(dupulicate)

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

        # reassign holders
        self.holder.set_block(block)
        block.holder.set_block(self)

        temp_holder = self.holder
        self.holder = block.holder
        block.holder = temp_holder
       
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
            self.swap_blocks(self.holder.get_neibouring_block("right"))
        elif self.speed[0] <= -Block._size:
            self.speed = (self.speed[0] + Block._size, self.speed[1])
            self.swap_blocks(self.holder.get_neibouring_block("left"))

        if self.speed[1] >= Block._size:
            self.speed = (self.speed[0], self.speed[1] - Block._size)
            self.swap_blocks(self.holder.get_neibouring_block("down"))
        elif self.speed[1] <= -Block._size:
            self.speed = (self.speed[0], self.speed[1] + Block._size)
            self.swap_blocks(self.holder.get_neibouring_block("up"))
        
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
        self.block = None 

        # neibouring holders
        self.neibours: dict[str, BlockHolder | None] = {
            "up": None,
            "down": None,
            "left": None,
            "right": None
        }

    def get_neibouring_block(self, neibour: str):
        if self.neibours[neibour] is None:
            return None 

        # shouldent be a error
        return self.neibours[neibour].get_block()

    def set_block(self, block: Block):
        self.block = block
        self.block.set_holder(self)

    def get_block(self):
        return self.block

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

    def on_spread(self, block: Block) -> bool:
        return False
    
    def update(self, block: Block):
        # check if spreading
        if self.spread_count == self.spread:
            # reset spread count
            if self.on_spread(block):
                self.spread_count = 0
        # increment spread count
        elif (self.spread_count < self.spread):
            self.spread_count += 1


class GasProperty(Property):
    def __init__(self) -> None:
        super().__init__()
        self.set_spread(30)

    @override
    def on_spread(self, block: Block) -> bool:
        for holder in block.holder.neibours.values():
            if holder is not None and holder.get_block() is not None:
                if holder.get_block().check_property(GasProperty) is True:
                    # check not the same block type
                    if type(holder.get_block()) == type(block):
                        continue
                    block.dupulicate(holder.get_block())
                    return True
        return False

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
        
