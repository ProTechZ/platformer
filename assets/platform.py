import pygame
from os import getenv
from dotenv import load_dotenv
from math import modf

load_dotenv()

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, *groups):
        super().__init__(*groups)

        self.SCREEN = screen
        self.WIDTH = width
        self.HEIGHT = height

        self.image = self._generate()
        self.rect = self.image.get_rect() 

    def _generate(self):
        base = getenv('BASE')
        platform_img = pygame.image.load(f"{base}\\platformer\\resources\\platform.png").convert()

        og_width = platform_img.get_width()
        pygame.transform.scale(platform_img, (og_width, self.HEIGHT)) # only scaling height

        # instead of stretching the image to fit the width, we just display multiple platforms right next to each other uptil the width
        num_loop = round(self.WIDTH / og_width)

        platform = pygame.Surface((self.WIDTH, self.HEIGHT)).convert_alpha()

        for i in range(int(num_loop) + 1):
            platform.blit(platform_img, (og_width * i, 0))

        # rounding the corners
        rounded_surface = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(rounded_surface, (255, 255, 255, 255), (0, 0, self.WIDTH, self.HEIGHT), border_radius=5)

        platform.blit(rounded_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

        return platform
        