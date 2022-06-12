import pygame
from settings import *
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprite):
        super().__init__(group)
        self.import_playe_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["right"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = player_speed
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.collision_sprite = collision_sprite
        self.on_floor = False
        self.status = "idle right"
        self.idle_status = 1
    def import_playe_assets(self):
        player_path = "../Graphics/Player/"
        self.animations = {"idle left": [], "idle right": [], "right": [], "left": []}

        for animations in self.animations.keys():
            full_path = player_path + animations
            self.animations[animations] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.direction.x = 1
        elif key[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if key[pygame.K_SPACE] and self.on_floor is True:
            self.direction.y = -self.jump_speed

    def get_status(self):
        if self.direction.x < 0:
            self.status = "left"
            self.idle_status = -1
        elif self.direction.x > 0:
            self.status = "right"
            self.idle_status = 1
        else:
            if self.idle_status == -1:
                self.status = "idle left"
            if self.idle_status == 1:
                self.status = "idle right"

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def horizontal_collision(self):
        for sprite in self.collision_sprite:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def verticle_collision(self):
        for sprite in self.collision_sprite:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y <= 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collision()
        self.apply_gravity()
        self.verticle_collision()
