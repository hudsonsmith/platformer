import pygame
from os import system

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, color, tile_size) -> None:
        super().__init__()
        self.image = pygame.Surface((tile_size / 2, tile_size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.tile_size = tile_size
        self.speed = tile_size / 10

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
        self.direction.x = -self.speed

    def move_right(self):
        self.direction.x = self.speed

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x
