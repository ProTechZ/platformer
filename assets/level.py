import pygame
from dotenv import load_dotenv
from os import getenv
from assets.platform import Platform

load_dotenv()

class Level:
    def __init__(self, screen):
        self.platforms = pygame.sprite.Group()

        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()

    def gen_platforms(self, platforms_details):
        for x, y, width, height in  platforms_details:
            platform = Platform(self.SCREEN, width, height)
            platform.rect.x = x
            platform.rect.y = y
            self.platforms.add(platform)

    def draw_ground(self):
        base = getenv('BASE')
        ground = pygame.image.load(f"{base}\\platformer\\resources\\ground.png").convert()

        for x in range(0, self.SCREEN_WIDTH, ground.get_width()):
            self.SCREEN.blit(ground, (x, self.SCREEN_HEIGHT - ground.get_height()))

class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)
        platforms_details = [
            (200, 475, 200, 50),
            (450, 400, 200, 50),
            (700, 325, 200, 50),
        ]

        self.gen_platforms(platforms_details)

