import pygame, sys
from settings import *
from level import Level
from level_data import main_level

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Infinity Quest")
pygame.display.set_icon(pygame.image.load("../Graphics/level images/icon.png"))
level = Level(main_level, screen)

while True:

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color["background"])
    level.run()
    pygame.display.update()
    clock.tick(60)
