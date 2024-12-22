import pygame

class Level:
    def __init__(self, screen):
        self.platforms = []

        self.SCREEN = screen

        self.PLATFORM_HEIGHT = 10
        self.PLATFORM_WIDTH = 50

    def draw_platforms(self, platforms_coords):
        for x, y in platforms_coords:
            pygame.draw.rect(self.SCREEN, (0, 0, 0), (x, y, self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))

    def draw_ground(self):
        ground = pygame.image.load(r"C:\Users\sheeb_gztgpqt\Desktop\Master Files\Coding\Machine Learning\platformer\images\ground.jpg").convert()

        self.SCREEN.blit(ground, (0, self.SCREEN.get_height() - ground.get_height()))
    
class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)

    def draw_platforms(self):
        platforms_coords = [(300, 300)]

        return super().draw_platforms(platforms_coords)
    
