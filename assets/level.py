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

        self.collision = ''
        self.prev_collision = ''

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
        player_b = player.y + player.image.get_height()
        player_t = player.y
        player_l = player.x
        player_r = player.x + player.SIZE

        platform_b = platform.rect.y + platform.HEIGHT
        platform_t = platform.rect.y
        platform_l = platform.rect.x
        platform_r = platform.rect.x + platform.WIDTH

        if pygame.rect.Rect(player.x, player.y, player.SIZE, player.image.get_height()).colliderect(platform.rect):
            # Top collision
            if player_b > platform_t and player.velocity_y > 0 and not player.action == 'jump_start':
                player.y = platform_t - player.image.get_height()
                player.velocity_y = 0
                player.set_idle()
                print('top')
                
            # Left collision
            elif player_r > platform_l and player_l < platform.rect.left:
                player.x = platform_l - player.SIZE

            # Right collision
            elif player_l < platform_r and player_r > platform_r:
                player.x = platform_r

            # Bottom collision
            elif player_t < platform_b and player_b > platform_b:
                player.y = platform_b
                player.velocity_y = 1

    def collide(self, platform: Platform):
        self.detect_collision(self.PLAYER, platform)

class Level1(Level):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        platforms_details = [
            (220, 475, 200, 50),
            (450, 400, 200, 50),
            (700, 325, 200, 50),
        ]

        self.gen_platforms(platforms_details)

