import pygame
from dotenv import load_dotenv
from os import getenv, path
from assets.platform import Platform
from assets.endpoint import EndPoint

import sys
sys.path.append(path.abspath(path.join('..')))
from constants import GROUND_LEVEL

load_dotenv()

class Level:
    def __init__(self, screen, player):
        self.platforms = pygame.sprite.Group()
        self.PLAYER = player
        self.ENDPOINT = EndPoint(60)

        self.SCREEN = screen
        self.SCREEN_WIDTH = self.SCREEN.get_width()
        self.SCREEN_HEIGHT = self.SCREEN.get_height()

    def draw_level(self):
        self._draw_ground()
        self.platforms.update()
        self.platforms.draw(self.SCREEN)
        self._draw_endpoint()

    def _draw_endpoint(self):
        last_platform = self.platforms.sprites()[-1]

        self.ENDPOINT.rect.x = (last_platform.rect.x + last_platform.WIDTH / 2) - self.ENDPOINT.image.get_width() / 2
        self.ENDPOINT.rect.y = last_platform.rect.y - self.ENDPOINT.image.get_height()

        self.SCREEN.blit(self.ENDPOINT.image, (self.ENDPOINT.rect.x, self.ENDPOINT.rect.y))

    def gen_platforms(self, platforms_details):
        for x, y, width, height in  platforms_details:
            platform = Platform(self.SCREEN, width, height)
            platform.rect.x = x
            platform.rect.y = y
            self.platforms.add(platform)

    def _draw_ground(self):
        base = getenv('BASE')
        ground = pygame.image.load(f"{base}\\platformer\\resources\\ground.png").convert()

        for x in range(0, self.SCREEN_WIDTH, ground.get_width()):
            self.SCREEN.blit(ground, (x, self.SCREEN_HEIGHT - ground.get_height()))

    def reached_endpoint(self):
        player_middle_x = self.PLAYER.x + self.PLAYER.SIZE / 2
        player_middle_y = self.PLAYER.y + self.PLAYER.image.get_height() /  2
        if self.ENDPOINT.rect.collidepoint(player_middle_x, player_middle_y):
            return True

    def detect_collision(self, platform: Platform):
        player_b = self.PLAYER.y + self.PLAYER.image.get_height()
        player_t = self.PLAYER.y
        player_l = self.PLAYER.x
        player_r = self.PLAYER.x + self.PLAYER.SIZE

        platform_b = platform.rect.y + platform.HEIGHT
        platform_t = platform.rect.y
        platform_l = platform.rect.x
        platform_r = platform.rect.x + platform.WIDTH

        if self.PLAYER.rect.colliderect(platform.rect):
            # Falling down
            if player_b >= platform_t and player_t < platform_t:
                tipping_point = player_r - 20

                # Falling from left
                if self.PLAYER.action == 'run_left' and tipping_point - self.PLAYER.MOVING_SPEED < platform_l:
                    self.PLAYER.set_jump_end()

                # Falling from right
                elif self.PLAYER.action == 'run_right' and tipping_point - self.PLAYER.MOVING_SPEED > platform_r:
                    self.PLAYER.set_jump_end()

            # Jumping on top of platform collision
            if player_b > platform_t and player_t < platform_t and self.PLAYER.velocity_y > 0 and self.PLAYER.action == 'jump_end':
                self.PLAYER.y = platform_t - self.PLAYER.image.get_height()
                self.PLAYER.velocity_y = 0
                self.PLAYER.set_idle()

                # if player jumped on the last platform, open the gate
                last_platform = self.platforms.sprites()[-1]
                if self.PLAYER.rect.colliderect(last_platform.rect):
                    self.ENDPOINT.open()
                
            # Left collision
            elif player_r >= platform_l and player_l < platform_l and self.PLAYER.y == GROUND_LEVEL :
                if self.PLAYER.move_while_running:
                    self.PLAYER.x = platform_l - self.PLAYER.SIZE
                self.PLAYER.move_while_running = False
                
            # Right collision
            elif player_l <= platform_r and player_r > platform_r and self.PLAYER.y == GROUND_LEVEL:
                if self.PLAYER.move_while_running:
                    self.PLAYER.x = platform_r
                self.PLAYER.move_while_running = False

            # Bottom collision
            elif player_t <= platform_b and player_b > platform_b and 'jump' in self.PLAYER.action:
                self.PLAYER.y = platform_b
                self.PLAYER.set_jump_end()
                self.PLAYER.velocity_y = 1
