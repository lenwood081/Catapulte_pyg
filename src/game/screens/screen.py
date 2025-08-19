from observers.observer import ObserverFactory

class Screen:
    def __init__(self, window): 
        # parent screen
        self.parent = None

        # queued screen
        self.queued_screen = self

        # framerate
        self.framerate = 60

        # base screen
        self.window = window
    
    def set_queued_screen(self, screen):
        self.queued_screen = screen
    
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
    # events = (events, keys_pressed, mouse_pressed, (mouse_x, mouse_y))
    def run(self, dt: float, events): 
        # reset queued screen
        self.queued_screen = self

        # inform observers
        ObserverFactory.get_instance().get_arrorK().notify(events[1])
        ObserverFactory.get_instance().get_mouse_left_click_pos().notify((events[2], events[3]))
        return self.queued_screen

