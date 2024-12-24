import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, *groups):
        super().__init__(*groups)

        self.WIDTH = width
        self.height = height