import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, color="grey") -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift) -> None:
        self.rect.x += x_shift
