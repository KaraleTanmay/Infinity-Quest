import pygame
from settings import color


class UI:
    def __init__(self, surface):
        self.display_surface = surface
        self.health_bar = pygame.image.load("../Graphics/gui/health bar.png")
        self.gauntlet = pygame.image.load("../Graphics/gui/gauntlet.png")
        self.font = pygame.font.Font("../Graphics/gui/Blaka-Regular.ttf", 40)
        self.health_bar_topleft = (70, 40)
        self.bar_max_width = 178
        self.bar_height = 40

    def show_health_bar(self, full_health, current_health):
        current_health_ratio = current_health / full_health
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, color["player"], health_bar_rect)
        self.display_surface.blit(self.health_bar, (20, 20))

    def show_collected_stones(self, group):
        self.display_surface.blit(self.gauntlet, (300, 20))
        for index, sprite in enumerate(group.sprites()):
            self.display_surface.blit(sprite.image, (340 + (index + 1) * 80, 40))
