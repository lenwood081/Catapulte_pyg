import pygame


"""
Simple manager of lib resources
singlton
"""


class LibManager:
    _instance = None

    def __init__(self):
        self.buttons: dict[str, pygame.Surface] = {}

    def get_button_surface(self, name: str):
        if name not in self.buttons:
            # fetch from lib
            path = f"lib/buttons/{name}"
            self.buttons[name] = pygame.image.load(path).convert_alpha()

        return self.buttons[name]

    @staticmethod
    def get_instance():
        if LibManager._instance is None:
            LibManager._instance = LibManager()
        return LibManager._instance
