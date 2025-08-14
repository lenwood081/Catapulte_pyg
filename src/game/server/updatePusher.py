"""
A singlton class that accepts the most recent game updates in a 
set form
It is also used to send game updates to all connected clients
"""

class UpdatePusher:
    instance = None

    def __init__(self):
        self.update_buffer = []

        self.frame_number = 0
        self.update_buffer[self.frame_number] = []

        self.active = False

    @staticmethod
    def get_instance():
        if UpdatePusher.instance is None:
            UpdatePusher.instance = UpdatePusher()
        return UpdatePusher.instance

    def set_frame_number(self, frame_number):
        if frame_number != self.frame_number:
            self.update_buffer[frame_number] = []
        self.frame_number = frame_number

    def add_update(self, update):
        if not self.active:
            return
        self.update_buffer[self.frame_number].append(update)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


