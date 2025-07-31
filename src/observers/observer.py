"""
Listens for a event
has a list of subscribers
calls there update method
singleton
"""
from types import FunctionType, MethodType
from typing import override

from pygame import K_DOWN, K_UP, K_LEFT, K_RIGHT

class Observer:
    def __init__(self):
        self.subscribers: list[Subscriber] = []

    def notify(self, information):
        for subscriber in self.subscribers:
            subscriber.on_event(information, self)

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def clear_subscribers(self):
        self.subscribers = []

"""
singleton class for creating and managing observers
"""
class ObserverFactory:
    instance = None

    def __init__(self):
        self.observers = {}

    def get_arrorK(self):
        if "ArrowKObserver" not in self.observers:
            self.observers["ArrowKObserver"] = ArrowKObserver()
        return self.observers["ArrowKObserver"]

    def get_mouse_left_click_pos(self):
        pass

    @staticmethod
    def get_instance():
        if not ObserverFactory.instance:
            ObserverFactory.instance = ObserverFactory()
        return ObserverFactory.instance

"""
A subscriber for a event type
"""
class Subscriber:
    def __init__(self):
        self.active = True
        self.event_methods: dict[Observer, MethodType] = {}

    def assign_event_method(self, observer: Observer, method: MethodType):
        self.event_methods[observer] = method
        

    def on_event(self, information, observer: Observer):
        """
        Override in subclasses
        """
        if not self.active:
            return

        # determine which method to run based on observer
        self.event_methods[observer](information)

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

"""
Have gone to go with super specific observers to reduce extra
calls
"""
class ArrowKObserver(Observer):
    def __init__(self):
        super().__init__()

    @override
    def notify(self, information):
        # information starts as key pressed dictionary
        info = {
            "up": information[K_UP],
            "down": information[K_DOWN],
            "left": information[K_LEFT],
            "right": information[K_RIGHT]
        }
        sum = (info["up"] or info["down"] or info["left"] or info["right"])
        if sum:
            super().notify(info)

class MouseLeftClickPosObserver(Observer):
    def __init__(self):
        super().__init__()

    @override
    def notify(self, information):
        # information = (mouse pressed, (mouse_x, mouse_y))

        # check if mouse left clicked
        pass
