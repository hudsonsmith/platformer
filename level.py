import pygame
from tiles import Tile

class Level(object):
    def __init__(self, level_data, surface, settings) -> None:
        self.display_surface = surface
        self.setup_level(level_data, settings)

    def setup_level(self, layout, settings):
        self.tiles = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index * settings.tile_size
                    y = row_index * settings.tile_size
                    tile = Tile((x, y), settings.tile_size)
                    self.tiles.add(tile)

    def run(self) -> None:
        self.tiles.draw(self.display_surface)
