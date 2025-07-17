import pygame

class Screen:
    def __init__(self, 
                 width, height): 
        # screen size
        self.width = width
        self.height = height

        # parent screen
        self.parent = None

        # framerate
        self.framerate = 60

        # include screen (background)
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def set_parent(self, parent):
        self.parent = parent

    def set_framerate(self, framerate):
        self.framerate = framerate

    def draw(self) -> None:
        # draw all game obejects
        pass

    def update(self) -> None:
        # update all game objects
        pass    

    # run the screen loop
    def run(self, dt: float, events): 
        return self

