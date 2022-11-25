import pygame
from level import Level

class Settings(object):
    def __init__(self):
        self.tile_size = 1

class Intro(Level):
    def __init__(self, screen):
        super().__init__(["X ", "X "], screen, Settings(), "white")

    def display(self):
        self.tiles.update(1)
