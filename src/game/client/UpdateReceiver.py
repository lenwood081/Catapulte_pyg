import json
from typing import override
from world.block import *

"""
A class that receives json string updates
translates them to json frames
Updates blocks scheduled for updating in reciever
Creates new blocks based on received updates
"""

class UpdateReceiver:
    _instance = None
    
    def __init__(self) -> None:
        self.update_buffer = []

        self.frame_number = 0
        
        self.frame = {}
        
        self.block_size = 0
        self.world_size = (0, 0)
        self.camera_size = (0, 0)

    @staticmethod
    def get_instance():
        if UpdateReceiver._instance == None:
            UpdateReceiver._instance = UpdateReceiver()
        return UpdateReceiver._instance

    def upload_frame(self, frame):
        self.frame = json.loads(frame)
        self.frame_number = self.frame["n"]

    def get_frame_number(self):
        return self.frame_number

    def unpack_start_data(self, world: type, camera: type):

        self.block_size = self.frame["f"][0]["block_size"]
        self.world_size = tuple(self.frame["f"][0]["world_size"])
        self.camera_size = tuple(self.frame["f"][0]["camera_size"])

        Block._size = self.block_size

        new_world = world(self.world_size)
        new_camera = camera(self.camera_size[0], self.camera_size[1])

        return (new_world, new_camera)

    def create_block(self, block_data):
        new_block = Block(
            tuple(block_data["p"]), 
            block_data["id"]
        ) 

        # add other attributes
        new_block.velocity = block_data["v"]
        new_block.speed = block_data["s"]
        new_block.color = block_data["c"]
        new_block.base_color = block_data["bc"]

        # add properties
        # TODO add properties

        """
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
        
        """

        return new_block

    def update_blocks(self, frame, world):
        pass

        







