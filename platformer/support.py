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
