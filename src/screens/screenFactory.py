import pygame
from screens.menus.mainMenu import MainMenu
from screens.screen import Screen

# a singleton factory that stores all screens to promote reuse of screen
# instances, particularly menus
class Screen_Factory:
    # static varibles
    instance = None

    def __init__(self):
        # screen type: screen instance
        self.screens: dict[str, Screen] = {}

    def start_menu_screen(self) -> Screen:
        if "mainMenu" not in self.screens:
            self.screens["mainMenu"] = MainMenu(600, 800) 

        return self.screens["mainMenu"]

    @staticmethod
    def get_instance():
        if Screen_Factory.instance is None:
            Screen_Factory.instance = Screen_Factory()
        return Screen_Factory.instance
