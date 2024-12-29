import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, *groups):
        super().__init__(*groups)

        self.SCREEN = screen

        self.WIDTH = width
        self.HEIGHT = height

    def draw(self, x, y):
        pygame.draw.rect(self.SCREEN, (173, 186, 57), (x, y, self.WIDTH, self.HEIGHT), border_top_left_radius=10, border_top_right_radius=10) #green
        pygame.draw.rect(self.SCREEN, (89,94,41), (x, y + self.HEIGHT * 1/5, self.WIDTH, self.HEIGHT * 1/5))
        pygame.draw.rect(self.SCREEN, (122, 87, 64), (x, y + self.HEIGHT * 2/5, self.WIDTH, self.HEIGHT * 3/5), border_bottom_left_radius=10, border_bottom_right_radius=10)