import pygame
from os import getenv
from constants import GROUND_LEVEL

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, size, *groups):
        super().__init__(*groups)

        self.SCREEN = screen
        self.SIZE = size

        self.MOVING_SPEED = 4
        self.jump_force_y = 8
        self.jump_force_x = 3
        self.velocity_y = 0
        self.velocity_x = 0

        self.x = 20
        self.y = GROUND_LEVEL

    def rescale_player(self, player, size):
        width = int(player.get_width())
        height = int(player.get_height())
        scale = size/width

        return pygame.transform.scale(player, (size, height * scale))

    def touch_ground(self):
        self.y = GROUND_LEVEL
        self.velocity_y = 0
        self.velocity_x = 0

    def flip_frames(self, frames):
        return [pygame.transform.flip(frame, True, False) for frame in frames]

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
        player_frames = self.flip_frames(player_frames)

        return [self.rescale_player(frame, self.SIZE) for frame in player_frames]

    def jump_start(self, left=False):
        base = getenv('BASE')
        player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Jump Start\\Player_Jump_Start_{i}.png") for i in range(6)]

        if left: 
            player_frames = self.flip_frames(player_frames)

        return [self.rescale_player(frame, self.SIZE) for frame in player_frames]

    def jump_loop(self, left=False):
        base = getenv('BASE')
        player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Jump Loop\\Player_Jump_Loop_{i}.png") for i in range(6)]

        if left: 
            player_frames = self.flip_frames(player_frames)

        return [self.rescale_player(frame, self.SIZE) for frame in player_frames]
    
    def jump_end(self, left=False):
        base = getenv('BASE')
        player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Falling Down\\Player_Falling_Down_{i}.png") for i in range(6)]
        
        if left: 
            player_frames = self.flip_frames(player_frames)

        return [self.rescale_player(frame, self.SIZE) for frame in player_frames]
    