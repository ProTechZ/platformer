import pygame
from dotenv import load_dotenv
from os import getenv
from assets.platform import Platform
from assets.player import Player
from constants import GROUND_LEVEL

load_dotenv()

class Level:
    def __init__(self, screen, player):
        self.platforms = pygame.sprite.Group()
        self.PLAYER = player

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

    def detect_collision(self, player: Player, platform: Platform):
        # Player bounding box
        player_b = player.y + player.image.get_height()
        player_t = player.y
        player_l = player.x
        player_r = player.x + player.SIZE

        # Platform bounding box
        platform_b = platform.rect.y + platform.HEIGHT
        platform_t = platform.rect.y
        platform_l = platform.rect.x
        platform_r = platform.rect.x + platform.WIDTH

        # collision left
        if player_r >= platform_l and player_b > platform_t and player_t < platform_b:
            if player.y < GROUND_LEVEL: 
                player.set_jump_end()
            elif not player.action == 'run_left':
                player.set_idle()


class Level1(Level):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        platforms_details = [
            (220, 475, 200, 50),
            (450, 400, 200, 50),
            (700, 325, 200, 50),
        ]

        self.gen_platforms(platforms_details)

