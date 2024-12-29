import pygame
from dotenv import load_dotenv
from os import getenv
from assets.platform import Platform

load_dotenv()

class Level:
    def __init__(self, screen):
        self.platforms = []

        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()

    def draw_platforms(self, platforms_details):
        for x, y, width, height in  platforms_details:
            platform = Platform(self.SCREEN, width, height)
            self.platforms.append(platform)
            platform.draw(x, y)

    def draw_ground(self):
        base = getenv('BASE')
        ground = pygame.image.load(f"{base}\\platformer\\resources\\ground.png").convert()

        for x in range(0, self.SCREEN_WIDTH, ground.get_width()):
            self.SCREEN.blit(ground, (x, self.SCREEN_HEIGHT - ground.get_height()))
    
class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_platforms(self):
        platforms_details = [(200, 500, 200, 50)]

        return super().draw_platforms(platforms_details)
    
