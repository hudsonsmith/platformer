import pygame
from tiles import Tile
from player import Player
from os import system

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





    def scroll_x(self) -> None:
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        tile_size = self.settings.tile_size

        right_pos = self.settings.res.current_w - (tile_size + player.width)
        left_pos = (player.width) + tile_size



        #########################################################################
        #                              RIGHT SCROLL                             #
        #########################################################################
        # If the player was scrolling right, allow them to come back to the left.
        if player_x > right_pos and direction_x == 0.0:
            self.world_shift = 0
            player.speed = 0

        # If the player goes to far right, scroll the screen.
        elif player_x > right_pos and direction_x > 0:
            player.right_boundary = True
            self.world_shift = -player.default_speed
            player.speed = 0



        #########################################################################
        #                              LEFT SCROLL                              #
        #########################################################################
        # If the player was scrolling right, allow them to come back to the left.
        if player_x < left_pos and direction_x == 0.0:
            self.world_shift = 0
            player.speed = 0

        # If the player goes to far right, scroll the screen.
        elif player_x < left_pos and direction_x < 0:
            player.left_boundary = True 
            self.world_shift = player.default_speed
            player.speed = 0

        
        # # Too far left.
        # elif player_x < left_pos:
        #     player.left_boundary = True
        #     self.world_shift = player.default_speed
        #     player.speed = 0


        # Flag logics, when the player is outside of the boundaries.

        # Is out of the left boundary.
        if player_x > left_pos:
            player.left_boundary = False 

        # Is out of the right boundary.
        if player_x < right_pos:
            player.right_boundary = False

        if player.right_boundary == False and player.left_boundary == False:
            self.world_shift = 0
            player.speed = player.default_speed


    def horizontal_movement_collision(self):
        player = self.player.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # Moving left.
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # Moving up.
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top

                # Moving down.
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom


    def run(self) -> None:
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()
        self.vertical_movement_collision()
        self.horizontal_movement_collision()

        self.player.draw(self.display_surface)

        self.scroll_x()