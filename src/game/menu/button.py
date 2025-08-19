import pygame
from observers.observer import Subscriber, ObserverFactory

"""
A clickable object
takes a image
does some action
"""
class Button(Subscriber):
    def __init__(self) -> None:
        super().__init__() # Subscriber

        # graphics 
        self.height = 50
        self.width = 100
        self.x = 0
        self.y = 0
        self.image = pygame.Surface((self.width, self.height))


        # add to arrow key observer
        ObserverFactory.get_instance().get_mouse_left_click_pos().add_subscriber(self)
        self.assign_event_method(ObserverFactory.get_instance().get_mouse_left_click_pos(), )

    def mosuse

    def set_image(self, image)
        self.image = image

    def on_click(self):
        # override
        print("button clicked") 

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        
