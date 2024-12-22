import pygame
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Level:
    def __init__(self, screen):
        self.platforms = []

        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()

        self.PLATFORM_HEIGHT = 10
        self.PLATFORM_WIDTH = 50

    def draw_platforms(self, platforms_coords):
        for x, y in platforms_coords:
            pygame.draw.rect(self.SCREEN, (0, 0, 0), (x, y, self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))

    def draw_ground(self):
        base = getenv('BASE')
        ground = pygame.image.load(f"{base}\\platformer\\images\\ground.jpg").convert()

        for x in range(0, self.SCREEN_WIDTH, ground.get_width()):
            self.SCREEN.blit(ground, (x, self.SCREEN_HEIGHT - ground.get_height()))
    
class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_platforms(self):
        platforms_coords = [(300, 300)]

        return super().draw_platforms(platforms_coords)
    
