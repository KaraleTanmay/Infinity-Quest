import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(color["tile"])
        self.rect = self.image.get_rect(topleft=pos)
