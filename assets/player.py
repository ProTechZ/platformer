import pygame

import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from constants import *
from frame_functions import idle, run, jump_start, jump_loop, jump_end

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, size, *groups):
        super().__init__(*groups)

        self.SCREEN = screen
        self.SIZE = size

        self.MOVING_SPEED = 4
        self.velocity_x = 0
        self.velocity_y = 0

        self.facing_left = False

        self.frames = idle()
        self.curr_frame = 0
        self.action = 'idle'
        self.move_while_running = True

        self.image = self.frames[self.curr_frame]
        self.rect = self.image.get_rect()

        self.x = 500
        self.y = GROUND_LEVEL

    @property
    def image(self):
        return self.frames[self.curr_frame]
    
    @image.setter
    def image(self, value):
        return value
    
    # only for the collision detection
    @property
    def rect(self):
        r = self.image.get_rect()
        r.x = self.x
        r.y = self.y
        return r
    
    @rect.setter
    def rect(self, value):
        return value

    def set_idle(self):
        self.frames = idle(left=self.facing_left)
        self.action = 'idle'

    def set_run_left(self):
        self.frames = run(left=True)
        self.curr_frame = 0
        self.action = 'run_left'
        self.move_while_running = True
        self.facing_left = True

    def set_run_right(self):
        self.frames = run()
        self.curr_frame = 0
        self.action = 'run_right'
        self.move_while_running = True
        self.facing_left = False

    def set_jump_start(self):
        self.action = 'jump_start'
        self.frames = jump_start(left=self.facing_left)
        self.curr_frame = 0
        self.velocity_y = 8
        self.velocity_x = 8

    def set_jump_loop(self):
        self.action = 'jump_loop'
        self.frames = jump_loop(left=self.facing_left)

    def set_jump_end(self):
        self.curr_frame = 0
        self.action = 'jump_end'
        self.frames = jump_end(left=self.facing_left)

    def run_right(self):
        if self.move_while_running:
            self.x += self.MOVING_SPEED

    def run_left(self):
        if self.move_while_running:
            self.x -= self.MOVING_SPEED

    def jump(self):     
        # if self.touching_rborder() or self.touching_lborder():
        #     self.action = 'jump_end'
        #     self.frames = jump_end(left=self.facing_left)
        #     self.velocity_y = self.jump_force_y
        #     self.velocity_x = 0
        
        if self.action == 'jump_start' or self.action == 'jump_loop':
            self.y -= (self.velocity_y **2)*0.5

            if self.velocity_y > 0:
                self.velocity_y -= .75

        elif self.action == 'jump_end':
            self.y += (self.velocity_y ** 2) *0.5
            self.velocity_y += 1

        self.x -= self.velocity_x if self.facing_left else -self.velocity_x

        if self.y >= GROUND_LEVEL:
            self.y = GROUND_LEVEL
            self.velocity_y = 10
            self.velocity_x = 0