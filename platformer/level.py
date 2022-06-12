import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.tiles = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()

        self.visible_sprites = Camera_group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup_level()

    def setup_level(self):
        for row_index, row in enumerate(levelmap):
            for col_index, col in enumerate(row):
                y = row_index * tilesize
                x = col_index * tilesize
                if col == "X":
                    Tile((x, y), [self.visible_sprites, self.collision_sprites])
                if col == "P":
                    self.player = Player((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)
                    self.player_group.add(self.player)

    def run(self):
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)


class Camera_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        camera_left = camera_borders["left"]
        camera_top = camera_borders["top"]
        camera_width = self.display_surface.get_size()[0] - (camera_left + camera_borders["right"])
        camera_height = self.display_surface.get_size()[1] - (camera_top + camera_borders["bottom"])

        self.camera_rect = pygame.Rect(camera_left, camera_top, camera_width, camera_height)

    def custom_draw(self, player):
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        self.offset = pygame.math.Vector2(self.camera_rect.left - camera_borders["left"],
                                          self.camera_rect.top - camera_borders["top"])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
