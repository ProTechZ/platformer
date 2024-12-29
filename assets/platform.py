import pygame
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, *groups):
        super().__init__(*groups)

        self.SCREEN = screen

        self.WIDTH = width
        self.HEIGHT = height

    def draw(self, x, y):
        base = getenv('BASE')
        platform = pygame.image.load(f"{base}\\platformer\\resources\\platform.png").convert_alpha()
        scaled = pygame.transform.scale(platform, (self.WIDTH, self.HEIGHT))

        # for rounded corners
        rounded_surface = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(rounded_surface, (255, 255, 255, 255), (0, 0, self.WIDTH, self.HEIGHT), border_radius=5)

        scaled.blit(rounded_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

        print(scaled.get_width())

        self.SCREEN.blit(scaled, (x, y))

        # for x in range(0, self.WIDTH, platform.get_width()):