import json

"""
A singlton class that accepts the most recent game updates in a 
set form
It is also used to send game updates to all connected clients
"""

class UpdatePusher:
    _instance = None

    def __init__(self):
        self.update_buffer = []

        self.frame_number = 0
        self.update_buffer.append([])

        self.active = False

    @staticmethod
    def get_instance():
        if UpdatePusher._instance is None:
            UpdatePusher._instance = UpdatePusher()
        return UpdatePusher._instance

    def increase_frame_number(self):
        self.update_buffer.append([])
        self.frame_number += 1

    def add_update(self, update):
        if not self.active:
            return
        self.update_buffer[self.frame_number].append(update)

    def get_update(self):
        frame = self.update_buffer[self.frame_number]
        self.update_buffer[self.frame_number] = []
        # convert to json format

        json_form = {
            "n": self.frame_number,
            "f": frame
        }
        return json.dumps(json_form) # json frame

    def activate(self):
        self.active = True

    def deactivate(self):
        self.update_buffer = []
        self.frame_number = 0
        self.update_buffer.append([])

        self.active = False

