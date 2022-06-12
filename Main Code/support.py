from csv import reader
from settings import tilesize
import pygame
from os import walk


def import_folder(path):
    image_list = []
    for _, __, image_files in walk(path):
        for image_file in image_files:
            full_path = path + "/" + image_file
            image = pygame.image.load(full_path).convert_alpha()
            image_list.append(image)
    return image_list


def import_csv_layout(path):
    map_layout = []
    with open(path) as map:
        level_layout = reader(map, delimiter=",")
        for row in level_layout:
            map_layout.append(row)
    return map_layout


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_number_x = int(surface.get_size()[0] // tilesize)
    tile_number_y = int(surface.get_size()[1] // tilesize)

    tile_list = []

    for row in range(tile_number_y):
        for col in range(tile_number_x):
            x = col * tilesize
            y = row * tilesize
            new_surface = pygame.Surface((tilesize, tilesize), flags=pygame.SRCALPHA)
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, tilesize, tilesize))
            tile_list.append(new_surface)

    return tile_list


def import_stones_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_number_x = 6
    tile_number_y = 1

    tile_list = []

    for row in range(tile_number_y):
        for col in range(tile_number_x):
            x = (col * 40)
            y = (row * 40)
            new_surface = pygame.Surface((40, 40), flags=pygame.SRCALPHA)
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, 40, 40))
            tile_list.append(new_surface)

    return tile_list
