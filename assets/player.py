import pygame

import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from constants import GROUND_LEVEL, idle

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

        self.frames = idle()
        self.curr_frame = 0
        self.action = 'idle'

        self.image = self.frames[self.curr_frame]
        self.rect = self.image.get_rect()

        self.x = 20
        self.y = GROUND_LEVEL

    @property
    def image(self):
        return self.frames[self.curr_frame]
    
    @image.setter
    def image(self, value):
        return value

    def touch_ground(self):
        self.y = GROUND_LEVEL
        self.velocity_y = 0
        self.velocity_x = 0
