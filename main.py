import pygame, sys
from tiles import Tile
from level import Level
from settings import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 200))

res = pygame.display.Info()
s = Settings(res)

level = Level(s.level_map, screen, s)



if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        level.run()

        pygame.display.update()
        clock.tick(60)
