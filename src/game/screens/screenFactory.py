import pygame
from screens.menus.mainMenu import MainMenu
from screens.game.mainGame import MainGame
from screens.game.serverGame import ServerGame
from screens.screen import Screen

# a singleton factory that stores all screens to promote reuse of screen
# instances, particularly menus
class Screen_Factory:
    # static varibles
    instance = None

    def __init__(self):
        # window
        height = 600
        width = 800
        self.window = pygame.display.set_mode((width, height))

        # screen type: screen instance
        self.screens: dict[str, Screen] = {}

    def main_menu_screen(self) -> Screen:
        if "MainMenu" not in self.screens:
            self.screens["mainMenu"] = MainMenu(self.window) 

        return self.screens["mainMenu"]

    def main_game_screen(self) -> Screen:
        if "MainGame" not in self.screens:
            self.screens["MainGame"] = MainGame(self.window) 

        return self.screens["MainGame"]

    def server_game_screen(self) -> Screen:
        if "ServerGame" not in self.screens:
            self.screens["ServerGame"] = ServerGame(self.window) 

        return self.screens["ServerGame"]

    @staticmethod
    def get_instance():
        if Screen_Factory.instance is None:
            Screen_Factory.instance = Screen_Factory()
        return Screen_Factory.instance
