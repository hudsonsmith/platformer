import pygame
from os import system

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, color, tile_size) -> None:
        super().__init__()
        self.width = tile_size / 2
        self.height = tile_size

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.tile_size = tile_size

        self.default_speed = tile_size / 10
        self.speed = self.default_speed

        # Vars that determine if the player has hit the level scrolling boundaries yet.
        self.right_boundary = False
        self.left_boundary = False


    def get_input(self):
        keys = pygame.key.get_pressed()

        W = keys[pygame.K_m] > 0
        A = keys[pygame.K_a] > 0
        S = keys[pygame.K_s] > 0
        D = keys[pygame.K_d] > 0

        # system("cls")

        # print(f"W: {W}")
        # print(f"A: {A}")
        # print(f"S: {S}")
        # print(f"D: {D}")

        if A:
            self.move_left()

        elif D:
            self.move_right()

        else:
            self.direction.x = 0

    def move_left(self):
        self.speed = self.default_speed
        self.direction.x = -self.speed

    def move_right(self):
        self.speed = self.default_speed
        self.direction.x = self.speed

    def update(self):
        self.get_input()

        # If the right boundary is not hit, move the player to the right.
        if self.direction.x > 0 and self.right_boundary == False:
            print(f"MOVING RIGHT: {self.direction.x}")
            self.rect.x += self.direction.x
        
        # If the left boundary is not hit, move the player to the left.
        elif self.direction.x < 0 and self.left_boundary == False:
            print(f"MOVING LEFT: {self.direction.x}")
            self.rect.x += self.direction.x

        if self.right_boundary == True and self.direction.x == 0.0:
            print(f"AUTO SCROLLING at speed: {self.speed}")

        # If the player is in the right boundary and the direction is going left, stop scrolling.
        if self.right_boundary == True and self.direction.x < 0:
            self.right_boundary = False
            self.rect.x += self.direction.x




