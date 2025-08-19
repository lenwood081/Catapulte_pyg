from typing import override
import pygame
from observers.observer import Subscriber, ObserverFactory

"""
A clickable object
takes a image
does some action
"""
class Button(Subscriber):
    def __init__(self, width=50, height=100) -> None:
        super().__init__() # Subscriber

        # graphics 
        self.height = height
        self.width = width
        self.x = 100
        self.y = 100
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

    def on_click(self):
        # override
        print("button clicked") 

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


