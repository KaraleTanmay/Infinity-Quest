import pygame, sys
from settings import *
from level import Level

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Infinity Quest")

level = Level()

while True:

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color["background"])
    level.run()
    pygame.display.update()
    clock.tick(60)
