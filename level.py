import pygame
from tiles import Tile
from player import Player

class Level(object):
    def __init__(self, level_data, surface, settings, tile_color="grey") -> None:
        self.display_surface = surface
        self.world_shift = 0
        self.tile_color = tile_color
        self.settings = settings

        # Run the setup after the internal settings are set.
        self.setup_level(level_data, settings)

    def setup_level(self, layout, settings):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * settings.tile_size
                y = row_index * settings.tile_size

                if cell == "X":
                    tile = Tile((x, y), settings.tile_size, self.tile_color)
                    self.tiles.add(tile)

                elif cell == "P":
                    player_sprite = Player((x, y), "red", settings.tile_size)
                    self.player.add(player_sprite)


    def run(self) -> None:
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()
        self.player.draw(self.display_surface)

        self.scroll_x()

    def scroll_x(self) -> None:
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        tile_size = self.settings.tile_size

        # If the player goes to far right, scroll the screen.
        if player_x > self.settings.res.current_w - (tile_size + player.width):
            self.world_shift = -(tile_size / 10)
            player.speed = 0

        elif player_x < (player.width) + tile_size:
            player.speed = 0
            self.world_shift = tile_size / 10
