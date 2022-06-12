import pygame
from settings import *
from support import import_csv_layout, import_cut_graphics, import_stones_cut_graphics
from tile import Statictile, Propertile, Gun, Lift
from player import Player
from slicer import Slicer, Gates, Arrow
from ui import UI


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = shift

        self.collected_sound = pygame.mixer.Sound("../Sounds/coin.wav")

        self.font = pygame.font.Font("../Graphics/gui/Blaka-Regular.ttf", 40)

        self.max_health = 100
        self.current_health = 100
        self.gun_status = False
        self.lift_status = "idle"
        self.ui = UI(self.display_surface)

        self.time = 0

        self.you_win = False

        player_layout = import_csv_layout(level_data["start"])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout, self.change_health)

        self.collected_stones_sprite = pygame.sprite.Group()

        temple_tiles_layout = import_csv_layout(level_data["temple tiles"])
        self.temple_tiles_sprite = self.create_sprite_group(temple_tiles_layout, "temple_tiles")

        cave_layout = import_csv_layout(level_data["cave"])
        self.cave_sprite = self.create_sprite_group(cave_layout, "cave")

        stones_layout = import_csv_layout(level_data["stones"])
        self.stones_sprite = self.create_sprite_group(stones_layout, "stones")

        rocks_layout = import_csv_layout(level_data["rocks"])
        self.rocks_sprite = self.create_sprite_group(rocks_layout, "rocks")

        shooter_layout = import_csv_layout(level_data["shooter"])
        self.shooter_sprite = self.create_sprite_group(shooter_layout, "shooter")

        arrow_layout = import_csv_layout(level_data["arrow"])
        self.arrow_sprite = self.create_sprite_group(arrow_layout, "arrow")

        pipe_layout = import_csv_layout(level_data["pipe"])
        self.pipe_sprite = self.create_sprite_group(pipe_layout, "pipe")

        slicer_layout = import_csv_layout(level_data["slicer"])
        self.slicer_sprite = self.create_sprite_group(slicer_layout, "slicer")

        controller_layout = import_csv_layout(level_data["controller"])
        self.controller_sprite = self.create_sprite_group(controller_layout, "controller")

        door_layout = import_csv_layout(level_data["end door"])
        self.door_sprite = self.create_sprite_group(door_layout, "end door")

        gates_layout = import_csv_layout(level_data["gates"])
        self.gates_sprite = self.create_sprite_group(gates_layout, "gates")

        liquid_layout = import_csv_layout(level_data["liquid"])
        self.liquid_sprite = self.create_sprite_group(liquid_layout, "liquid")

        gun_layout = import_csv_layout(level_data["gun"])
        self.gun_sprite = self.create_sprite_group(gun_layout, "gun")

        lift_layout = import_csv_layout(level_data["lift"])
        self.lift_sprite = self.create_sprite_group(lift_layout, "lift")

        constrains_layout = import_csv_layout(level_data["constrains"])
        self.constrains_sprite = self.create_sprite_group(constrains_layout, "constrains")

        arrow_constrains_layout = import_csv_layout(level_data["arrow constrains"])
        self.arrow_constrains_sprite = self.create_sprite_group(arrow_constrains_layout, "arrow constrains")

        self.visible_sprites = Camera_group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        visible_sprite = self.cave_sprite.sprites() + self.slicer_sprite.sprites() + self.rocks_sprite.sprites() + \
                         self.temple_tiles_sprite.sprites() + self.stones_sprite.sprites() + self.arrow_sprite.sprites() + \
                         self.shooter_sprite.sprites() + self.pipe_sprite.sprites() + \
                         self.player.sprites() + self.goal.sprites() + self.controller_sprite.sprites() + \
                         self.liquid_sprite.sprites() + self.gates_sprite.sprites() + self.door_sprite.sprites() + \
                         self.gun_sprite.sprites() + self.lift_sprite.sprites()

        self.visible_sprites.add(visible_sprite)

    def create_sprite_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != "-1":
                    x = col_index * tilesize
                    y = row_index * tilesize

                    if type == "temple_tiles":
                        tile_list = import_cut_graphics("../Graphics/level images/temple tiles.png")
                        tile_surface = tile_list[int(col)]
                        sprite = Statictile(tilesize, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == "cave":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/cave.png")
                        sprite_group.add(sprite)

                    if type == "shooter":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/shooter.png")
                        sprite_group.add(sprite)

                    if type == "arrow":
                        if col == "0":
                            sprite = Arrow(x, y + 20, 1)
                            sprite_group.add(sprite)
                        if col == "1":
                            sprite = Arrow(x, y + 20, -1)
                            sprite_group.add(sprite)

                    if type == "pipe":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/pipe.png")
                        sprite_group.add(sprite)

                    if type == "slicer":
                        sprite = Slicer(tilesize, x, y + 40)
                        sprite_group.add(sprite)

                    if type == "constrains":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/red.png")
                        sprite_group.add(sprite)

                    if type == "arrow constrains":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/red.png")
                        sprite_group.add(sprite)

                    if type == "stones":
                        tile_list = import_stones_cut_graphics("../Graphics/level images/Layer 4.png")
                        tile_surface = tile_list[int(col)]
                        sprite = Statictile(tilesize, x + 20, y + 20, tile_surface)
                        sprite_group.add(sprite)

                    if type == "rocks":
                        tile_list = import_stones_cut_graphics("../Graphics/level images/rocks.png")
                        tile_surface = tile_list[int(col)]
                        sprite = Statictile(tilesize, x + 20, y + 40, tile_surface)
                        sprite_group.add(sprite)

                    if type == "controller":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/controller.png")
                        sprite_group.add(sprite)

                    if type == "end door":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/door.png")
                        sprite_group.add(sprite)

                    if type == "gates":
                        sprite = Gates(x, y)
                        sprite_group.add(sprite)

                    if type == "liquid":
                        sprite = Propertile(tilesize, x, y, "../Graphics/level images/liquid.png")
                        sprite_group.add(sprite)

                    if type == "gun":
                        sprite = Gun(x, y + 20)
                        sprite_group.add(sprite)

                    if type == "lift":
                        sprite = Lift(x, y + 40)
                        sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout, change_health):
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tilesize
                y = row_index * tilesize
                if col == "0":
                    self.sprite = Player((x, y), self.display_surface, change_health)
                    self.player.add(self.sprite)

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        collision_sprite = self.temple_tiles_sprite.sprites() + self.pipe_sprite.sprites() + \
                           self.shooter_sprite.sprites() + \
                           self.gates_sprite.sprites() + \
                           self.lift_sprite.sprites()
        for sprite in collision_sprite:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left


    def verticle_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collision_sprite = self.temple_tiles_sprite.sprites() + self.pipe_sprite.sprites() + \
                           self.shooter_sprite.sprites() + \
                           self.lift_sprite.sprites()
        for sprite in collision_sprite:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y <= 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_floor = True
        if player.on_floor and player.direction.y != 0:
            player.on_floor = False

    def change_health(self, amount):
        self.current_health -= amount

    def slicer_reverse(self):
        for slicer in self.slicer_sprite.sprites():
            if pygame.sprite.spritecollide(slicer, self.constrains_sprite, False):
                slicer.reverse_speed()

    def gates_reverse(self):
        for gate in self.gates_sprite.sprites():
            if pygame.sprite.spritecollide(gate, self.constrains_sprite, False):
                gate.reverse_speed()

    def arrow_reset(self):
        for arrow in self.arrow_sprite.sprites():
            if pygame.sprite.spritecollide(arrow, self.arrow_constrains_sprite, False):
                arrow.reset_location()

    def check_stone_collision(self):
        for sprite in self.stones_sprite.sprites():
            if sprite.rect.colliderect(self.player.sprite.rect):
                self.collected_stones_sprite.add(sprite)
                sprite.rect.y = -300
                self.collected_sound.play()

    def acid_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.liquid_sprite, False):
            self.player.sprite.get_damage(15)

    def slicer_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.slicer_sprite, False):
            self.player.sprite.get_damage(20)

    def arrow_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.arrow_sprite, False):
            self.player.sprite.get_damage(10)

    def gun_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.gun_sprite, True):
            self.gun_status = True

    # def door_collision(self):
    #     for sprite in self.door_sprite.sprites():
    #         if sprite.rect.colliderect(self.player.sprite):
    #             self.you_won()

    def lift_function(self):
        for sprite in self.controller_sprite.sprites():
            if sprite.rect.colliderect(self.player.sprite):
                self.lift_status = "up"
                self.time = pygame.time.get_ticks()
        lift_speed = 5
        if self.lift_status == "up":
            self.player.sprite.rect.y -= lift_speed
            for sprite in self.lift_sprite.sprites():
                sprite.rect.y -= lift_speed
                if sprite.rect.y < (4 * tilesize):
                    self.lift_status = "idle down"

    def lift_down(self):
        if self.player.sprite.rect.y <= 9 * tilesize and self.player.sprite.rect.x >= 4 * tilesize \
                and self.lift_status == "idle down":
            for sprite in self.lift_sprite.sprites():
                sprite.rect.y += 5
                if sprite.rect.y >= (9 * tilesize) - 40:
                    self.lift_status = "idle"

    def gate_collision(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.gates_sprite, False):
            for sprite in self.gates_sprite.sprites():
                if sprite.rect.x < self.player.sprite.rect.x < sprite.rect.x + 80:
                    self.player.sprite.get_damage(40)

    def zero_health(self):
        if self.current_health <= 0:
            self.game_over()

    def game_over(self):
        self.visible_sprites.empty()
        self.display_surface.blit(pygame.image.load("../Graphics/level images/game over.png").convert_alpha(),
                                  (300, 180))
        display_text = self.font.render("Rerun the game to play again", False, "#FFD700")
        display_text_rect = display_text.get_rect(topleft=(400, 600))
        self.display_surface.blit(display_text, display_text_rect)

    def you_won(self):
        list = self.collected_stones_sprite.sprites()

        if pygame.sprite.spritecollide(self.player.sprite, self.door_sprite, False):
            if len(list) != 6:
                self.player.sprite.rect.x = self.door_sprite.sprites()[0].rect.x - 40
            if len(list) == 6:
                self.visible_sprites.empty()
                self.you_win = True

    def won(self):
        if self.you_win is True:
            self.display_surface.blit(pygame.image.load("../Graphics/level images/you won.png").convert_alpha(),
                                      (300, 180))
            display_text = self.font.render("Rerun the game to play again", False, "#FFD700")
            display_text_rect = display_text.get_rect(topleft=(400, 600))
            self.display_surface.blit(display_text, display_text_rect)

    def run(self):

        self.visible_sprites.update(self.world_shift)
        self.gate_collision()
        self.horizontal_collision()
        self.verticle_collision()
        self.constrains_sprite.update(self.world_shift)
        self.slicer_reverse()
        self.gates_reverse()
        self.arrow_reset()
        self.you_won()
        self.won()
        self.visible_sprites.custom_draw(self.sprite)
        self.check_stone_collision()
        self.acid_collision()
        self.slicer_collision()
        self.arrow_collision()
        self.gun_collision()
        self.lift_function()
        self.lift_down()
        self.zero_health()
        self.ui.show_health_bar(self.max_health, self.current_health)
        self.ui.show_collected_stones(self.collected_stones_sprite)


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
