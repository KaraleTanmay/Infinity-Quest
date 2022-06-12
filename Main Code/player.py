import pygame
from settings import *
from support import import_folder
from math import sin


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface, change_health):
        super().__init__()
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["right"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = player_speed
        self.jump_speed = jump_speed
        self.gravity = gravity

        self.on_floor = False
        self.status = "idle right"
        self.idle_status = 1

        self.change_health = change_health
        self.invincible = False
        self.invincibility_duration = 600
        self.hurt_time = 0

        self.jump_sound = pygame.mixer.Sound("../Sounds/jump.wav")
        self.hit_sound = pygame.mixer.Sound("../Sounds/hit.wav")

    def import_player_assets(self):
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

        if self.invincible:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

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
            self.jump_sound.play()

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

    def get_damage(self, health):
        if not self.invincible:
            self.change_health(health)
            self.hit_sound.play()
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

    def update(self, shift):
        self.input()
        self.get_status()
        self.animate()
        self.invincibility_timer()
        self.wave_value()
        self.rect.y -= shift
