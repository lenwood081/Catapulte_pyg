"""
Camera that moves with arrow keys
"""

from typing import override
from camera.camera import Camera
from observers.observer import Subscriber, ObserverFactory

class DevCamera(Camera, Subscriber):
    def __init__(self, width, height):
        super().__init__(width, height)
        Subscriber.__init__(self)
        
        # add to arrow key observer
        ObserverFactory.get_instance().get_arrorK().add_subscriber(self)

    @override
    def on_event(self, information):
        super().on_event(information)
        if information["up"]:
            self.y += 5
        if information["down"]:
            self.y -= 5
        if information["left"]:
            self.x += 5
        if information["right"]:
            self.x -= 5
