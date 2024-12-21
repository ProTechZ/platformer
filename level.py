import pygame

class Level:
    def __init__(self, num_platforms, screen):
        self.num_platforms = num_platforms
        self.platforms = []

        self.SCREEN = screen

        self.PLATFORM_HEIGHT = 10
        self.PLATFORM_WIDTH = 50


    def draw_platforms(self, platforms_coords):
        for i in range(self.num_platforms):
            x, y = platforms_coords[i]
            pygame.draw.rect(self.SCREEN, (0, 0, 0), (x, y, self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))      
    
