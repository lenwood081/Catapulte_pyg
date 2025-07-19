"""
A simple obsidian surrounded world for testing
during development
"""

import pygame
from world.world import World

class TestWorld(World):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size)
        self.obsidian_border()


