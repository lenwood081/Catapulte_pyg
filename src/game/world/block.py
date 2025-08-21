"""
Most basic unit in world
"""

from typing import override
from observers.observer import Subscriber, ObserverFactory
from server.updatePusher import UpdatePusher
import pygame


class Block(Subscriber):
    _size = 8
    _block_count = 0

    def __init__(self, pos: tuple[float, float], id: int = -1) -> None:
        super().__init__()

        self.__class__._block_count += 1

        # id is -1 if it is a new block, else it is given a id if it is merely a reflection of a server block
        if id == -1:
            self.id = self.__class__._block_count
        else:
            self.id = id

        # block position
        self.x = pos[0]
        self.y = pos[1]

        self.holder: BlockHolder

        # properies of the block
        self.properties: list[Property] = []

        # graphics of block
        self.base_color = (255, 0, 0)
        self.color = self.base_color
        self.surface = pygame.surface.Surface((Block._size, Block._size))
        self.surface.fill(self.color)

        # free flight properties
        self.velocity: tuple[float, float] = (0, 0)

        # must exceed size in either dimesion to move
        self.speed: tuple[float, float] = (0, 0)

        # determines whether or not to draw
        self.to_draw = True

        # important state check (True if updated in last loop, False if not)
        self.update_state = False
        self.scheduled_to_update = True

    def __eq__(self, other):
        if not isinstance(other, Block):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def get_if_updated(self) -> bool:
        return self.update_state

    def simple_varience(self, low: int, high: int) -> int:
        difference = (high - low)
        value = low + self.__class__._block_count % difference
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
        self.set_color(self.color)

    def set_color(self, color):
        self.color = color
        self.surface.fill(color)

    def set_holder(self, holder):
        self.holder = holder

    def add_velocity(self, velocity: tuple[float, float], max: tuple[float, float] = (0,0)):
        x = self.velocity[0] + velocity[0]
        y = self.velocity[1] + velocity[1]

        if max[0] != 0:
            x = max[0] if x > max[0] else x
            x = -max[0] if x < -max[0] else x

        if max[1] != 0:
            y = max[1] if y > max[1] else y
            y = -max[1] if y < -max[1] else y
        
        self.velocity = (x, y)


    def kill_x_velocity(self):
        self.velocity = (0, self.velocity[1])
        self.speed = (0, self.speed[1])

    def kill_y_velocity(self):
        self.velocity = (self.velocity[0], 0)
        self.speed = (self.speed[0], 0)

    def dupulicate(self, block):
        dupulicate = self.__class__((block.x, block.y))
            
        # change holder
        dupulicate.holder = block.holder
        dupulicate.holder.set_block(dupulicate)

        # TODO send dupulicate update to update pusher

    def swap_blocks(self, block):
        """
        Swaps two blocks positions
        """
         
        self.update_state = True
        block.update_state = True
        
        # TODO send swap update to update pusher

        temp = self.x
        self.x = block.x
        block.x = temp
        
        temp = self.y
        self.y = block.y
        block.y = temp

        # reassign holders
        temp_holder = self.holder
        block.holder.set_block(self)
        temp_holder.set_block(block)
       
    def move(self, dt: float):
        """
        Updates the blocks speed and if nessicary moves and
        swaps the blocks positions
        """

        if self.velocity[0] == 0 and self.velocity[1] == 0:
            return

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

        # TODO: transform to blit on surface call (avoids expensive draw calls)
        surface.blit(self.surface, (self.x, self.y))

        #pygame.draw.rect(surface, self.color, 
        #                (self.x, self.y, Block._size, Block._size)) 



    def update(self, dt: float):
        self.update_state = False
        if not self.scheduled_to_update:
            self.color = self.base_color
            return

        self.color = (100, 0, 0) # DEBUGGING
        self.scheduled_to_update = False

        # update all properties
        for property in self.properties:
            self.update_state = (property.update(self) or self.update_state)

        # update any movement
        self.move(dt)

        if self.update_state:
            # if sending updates compile state
            if UpdatePusher.get_instance().active:
                UpdatePusher.get_instance().add_update(self.summerise_block_state())
            self.scheduled_to_update = True

    def summerise_block_state(self):
        # TODO: Complile to json form for sending over network 

        state = {
            "p": (self.x, self.y),
            "v": self.velocity,
            "s": self.speed,
            "id": self.id,
            "c": self.color,
            "bc": self.base_color,
            # add all properties into a dictionary
            "props": [ {
                "s": property.spread,
                "sc": property.spread_count,
                "n": property.name,
            } for property in self.properties]
        }
        
        return state

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
        return self.neibours[neibour].block

    def set_block(self, block: Block):
        self.block = block
        self.block.set_holder(self)

    def draw(self, surface: pygame.surface.Surface):
        if self.block is None:
            return
        self.block.draw(surface)

    def determine_updates(self):
        if self.block is None:
            return

        if self.block.get_if_updated():
            # update all neibours
            for neibour in self.neibours.values():
                if neibour is not None:
                    if neibour.block is not None:
                        neibour.block.scheduled_to_update = True

    def update(self, dt: float):
        if self.block is None:
            return
        self.block.update(dt)

"""
A property of a block
"""
class Property:
    def __init__(self) -> None:
        # spread value (how many turns to spread) (-1 = no spread)
        self.spread: int = -1
        self.spread_count: int = 0
        self.name = "base"

    def set_spread(self, spread: int):
        self.spread = spread

    def on_spread(self, block: Block) -> bool:
        return False
    
    def update(self, block: Block) -> bool:
        """
        return True if there was change
        """

        # check if spreading
        if self.spread_count == self.spread:
            # reset spread count
            if self.on_spread(block):
                self.spread_count = 0
                return True
        # increment spread count
        elif (self.spread_count < self.spread):
            self.spread_count += 1
            return True

        return False


class GasProperty(Property):
    def __init__(self) -> None:
        super().__init__()
        self.set_spread(10)
        self.name = "gas"

    @override
    def on_spread(self, block: Block) -> bool:
        for holder in block.holder.neibours.values():
            if holder is not None and holder.block is not None:
                if holder.block.check_property(GasProperty) is True:
                    # check not the same block type
                    if type(holder.block) == type(block):
                        continue
                    block.dupulicate(holder.block)
                    return True
        return False

class SolidProperty(Property):
    def __init__(self) -> None:
        super().__init__()
        self.name = "solid"

class BreakProperty(Property):
    def __init__(self) -> None:
        super().__init__()
        self.name = "break"

class GravityProperty(Property):
    def __init__(self, terminal_velocity: float = 4) -> None:
        super().__init__()
        self.gravity: float = 1/16
        self.terminal_velocity: float = terminal_velocity
        self.name = "gravity"
        
    @override     
    def update(self, block: Block) -> bool:
        # check if a solid block exists below
        if block.holder.get_neibouring_block("down") is None or block.holder.get_neibouring_block("down").check_property(SolidProperty) is False:
            block.add_velocity((0, self.gravity), max=(0, self.terminal_velocity))
            return True
        else:
            if block.velocity[1] == 0:
                return False
            block.kill_y_velocity()
        return True

class FireProperty(Property):
    def __init__(self) -> None:
        super().__init__()
        self.name = "fire"
        
