import json

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
