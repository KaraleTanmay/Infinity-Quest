import pygame
from tile import Propertile


class Slicer(Propertile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, "../Graphics/level images/slicer.png")
        self.speed = 4

    def move(self):
        self.rect.x += self.speed

    def reverse_speed(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.move()


class Gates(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../Graphics/level images/gates.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def move(self):
        self.rect.y += self.speed

    def reverse_speed(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.y += shift
        self.move()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        image = pygame.image.load("../Graphics/level images/arrow.png").convert_alpha()
        if direction == 1:
            self.image = image
        if direction == -1:
            self.image = pygame.transform.flip(image, True, False)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 8 * direction
        self.x = x

    def move(self):
        self.rect.x += self.speed

    def reset_location(self):
        self.rect.x = self.x

    def update(self, shift):
        self.rect.x += shift
        self.move()
