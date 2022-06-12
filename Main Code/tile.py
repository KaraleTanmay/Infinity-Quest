import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        # self.rect.x -= shift
        self.rect.y -= shift


class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../Graphics/level images/gun.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        # self.rect.x -= shift
        self.rect.y -= shift


# class Gates(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.image.load("../Graphics/level images/gates.png").convert_alpha()
#         self.rect = self.image.get_rect(topleft=(x, y))
#
#     def update(self, shift):
#         # self.rect.x -= shift
#         self.rect.y -= shift


class Lift(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../Graphics/level images/lift.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        # self.rect.x -= shift
        self.rect.y -= shift


class Statictile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface


class Propertile(Statictile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y, pygame.image.load(path).convert_alpha())
