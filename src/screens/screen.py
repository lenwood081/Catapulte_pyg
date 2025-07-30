class Screen:
    def __init__(self, window): 
        # parent screen
        self.parent = None

        # framerate
        self.framerate = 60

        # base screen
        self.window = window
    
    def set_parent(self, parent):
        self.parent = parent

    def set_framerate(self, framerate):
        self.framerate = framerate

    def draw(self) -> None:
        # draw all game obejects
        pass

    def update(self, dt: float) -> None:
        # update all game objects
        pass    

    # run the screen loop
    def run(self, dt: float, events): 
        return self

