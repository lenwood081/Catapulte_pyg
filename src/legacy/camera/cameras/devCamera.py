"""
Camera that moves with arrow keys
"""

from camera.camera import Camera
from observers.observer import Subscriber, ObserverFactory

class DevCamera(Camera, Subscriber):
    def __init__(self, width, height):
        super().__init__(width, height)
        super(Camera, self).__init__()
        
        # add to arrow key observer
        ObserverFactory.get_instance().get_arrorK().add_subscriber(self)
        self.assign_event_method(ObserverFactory.get_instance().get_arrorK(), self.on_arrow_key)

    def on_arrow_key(self, information):
        if information["up"]:
            self.y += 5
        if information["down"]:
            self.y -= 5
        if information["left"]:
            self.x += 5
        if information["right"]:
            self.x -= 5



