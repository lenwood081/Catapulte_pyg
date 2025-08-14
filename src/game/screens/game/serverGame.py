from screens.screen import Screen
from camera.cameras.devCamera import DevCamera
from world.worldTypes.testWorld import TestWorld

"""
Server Game, authorative as to the game state
recives infromation from clients
tcp connections to clients
sends updated blocks at each tick
"""

class ServerGame(Screen):
    def __init__(self, window):
        super().__init__(window)

        self.world = TestWorld((800, 600))
        self.camera = DevCamera(800, 600)


