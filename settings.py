import pygame

class Settings(object):
    def __init__(self, res):
        self.level_map = [
            "         ",
            "         ",
            "         ",
            "XX       ",
            "XX       ",
            "XXXX  X  ",
            "XX       ",
            "XX      X",
            "XX       ",
            "XXXX    X",
            "XXXX    X",
            "XXXX    X",
            "XXXX    X",
            "XXXX    X",
            "XXXX    X",
            "XXXX    X",
            "XXXX    X",
        ]

        self.tile_size = res.current_h / len(self.level_map)
