import pygame
from os import getenv
import cv2

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, size, *groups):
        super().__init__(*groups)

        self.SCREEN = screen
        self.SIZE = size

    def rescale_player(self, player, size):
        width = int(player.get_width())
        height = int(player.get_height())
        scale = size/width
        
        return pygame.transform.scale(player, (size, height * scale))

    def idle(self):
        base = getenv('BASE')
        player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Idle\\Player_Idle_{i}.png") for i in range(18)]

        return [self.rescale_player(frame, self.SIZE) for frame in player_frames]

    def run_right(self):
        base = getenv('BASE')
        player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Running\\Player_Running_{i}.png") for i in range(12)]

        return [self.rescale_player(frame, self.SIZE) for frame in player_frames]
    
    def run_left(self):
        base = getenv('BASE')
        player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Running\\Player_Running_{i}.png") for i in range(12)]
        player_frames = [pygame.transform.flip(frame, True, False) for frame in player_frames]

        return [self.rescale_player(frame, self.SIZE) for frame in player_frames]
    