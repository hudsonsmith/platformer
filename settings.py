import pygame

class Settings(object):
    def __init__(self, res):
        self.level_map = [
            "XXXX  X  ",
            "XX       ",
            "XX      X",
            "XX P     ",
            "XXXX    X",
            "XXXX    X",
            "XXXX    X",
            "XXXXXXXXX",
        ]

        self.tile_size = res.current_h / len(self.level_map)
