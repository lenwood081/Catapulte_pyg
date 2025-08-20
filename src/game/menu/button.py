from typing import override
import pygame
from observers.observer import Subscriber, ObserverFactory

"""
A clickable object
takes a image
does some action
"""
class Button(Subscriber):
    def __init__(self, width=100, height=50, x=100, y=100) -> None:
        super().__init__() # Subscriber

        # graphics 
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))

        # add to arrow key observer
        ObserverFactory.get_instance().get_mouse_left_click_pos().add_subscriber(self)
        self.assign_event_method(ObserverFactory.get_instance().get_mouse_left_click_pos(), self.mouse_click)

    def mouse_click(self, information):
        # information = (mouse_x, mouse_y)
        # determine if clicked in button
        
        if information[0] > self.x and information[0] < self.x + self.width:
            if information[1] > self.y and information[1] < self.y + self.height:
                self.on_click()

    def set_image(self, image):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

    def scale_image(self, factor: float):
        # TODO: scale image without losing quality

        self.image = pygame.transform.scale_by(self.image, factor)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def on_click(self):
        # override
        print("button clicked") 

    def set_dimensions(self, width=None, height=None, x=None, y=None):
        self.width = width if width is not None else self.width
        self.height = height if height is not None else self.height
        self.x = x if x is not None else self.x
        self.y = y if y is not None else self.y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        

"""
Screen change button
on click will queue a screen change
"""
class ScreenChangeButton(Button):
    def __init__(self, screen_parent, screen_target: type) -> None:
        super().__init__()
        self.parent = screen_parent
        self.target_type = screen_target

    @override
    def on_click(self):
        # super().on_click()
        from screens.screenFactory import Screen_Factory
        self.parent.set_queued_screen(Screen_Factory.get_instance().get_screen(self.target_type))


