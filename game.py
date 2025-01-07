import pygame

from hand_detection import HandDetectorWindow
from assets.level import Level1
from assets.player import Player
from assets.platform import Platform
from constants import FPS, BASE_GRAVITY, GROUND_LEVEL
import math


pygame.init()

class Game:
    def __init__(self, width, height):
        self.WIDTH = int(width)
        self.HEIGHT = int(height)
        self.SCREEN = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.GRAVITY = BASE_GRAVITY
        
        self.CLOCK = pygame.time.Clock()
        self.frame_counter = 0
        self.FRAME_DELAY = 5

        self.CAMERA = HandDetectorWindow()

        self.is_running = True

        self.levels = [Level1(self.SCREEN)]
        self.curr_level_ind = 0

        self.player = Player(self.SCREEN, 100)
        self.facing_left = False

        self.player_action = 'idle'
        self.player_frames = self.player.idle()
        self.curr_player_frame = 0

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.is_running=False 
                if event.key == pygame.K_LEFT:
                    if self.player_action == 'idle' or self.player_action == 'run_right':
                        self.player_frames = self.player.run_left()
                        self.player_action = 'run_left'
                        self.facing_left = True

                if event.key == pygame.K_RIGHT:
                    if self.player_action == 'idle' or self.player_action == 'run_left':
                        self.player_frames = self.player.run_right()
                        self.player_action = 'run_right'
                        self.facing_left = False

                if event.key == pygame.K_SPACE:
                    if not 'jump' in self.player_action:
                        # self.facing_left = self.player_action == 'run_left'

                        self.player_action = 'jump_start'
                        self.player.velocity_y = self.player.jump_force_y
                        self.player.velocity_x = self.player.jump_force_x
                        self.player_frames = self.player.jump_start(left=self.facing_left)
                        self.curr_player_frame = 0

    def camera(self):
        camera, movement = self.CAMERA.start()
                                                                                                                                                                                                                                                                                        
        if camera is None:
            self.is_running = False
        else:       
            self.SCREEN.blit(camera, (0, 0))
            return movement

    def extend_frames(self):
        self.frame_counter += 1
        if self.frame_counter >= self.FRAME_DELAY:
            self.curr_player_frame += 1
            self.frame_counter = 0

    def jump(self):
        self.extend_frames()
        
        if self.player_action == 'jump_start' or self.player_action == 'jump_loop':
            self.player.velocity_y -= self.GRAVITY
            self.player.y -= self.player.velocity_y

        elif self.player_action == 'jump_end':
            self.player.velocity_y += self.GRAVITY
            self.player.y += self.player.velocity_y

        self.GRAVITY += 0.02
        self.player.x -= self.player.velocity_x if self.facing_left else -self.player.velocity_x

        if self.player.y >= GROUND_LEVEL + 5:
            self.player.touch_ground()
            self.player_frames = self.player.idle(left=self.facing_left)
            self.player_action = 'idle'
            self.GRAVITY = BASE_GRAVITY

    def run(self):
        while self.is_running:
            self.CLOCK.tick(FPS)
            self.event_loop()

            movement = self.camera()
            level = self.levels[self.curr_level_ind]

            self.SCREEN.fill((255, 255, 255))

            # resets the frame count if it reaches the end of the animation
            if self.curr_player_frame >= len(self.player_frames) - 1:
                self.curr_player_frame = 0
                
                if self.player_action == 'jump_start':
                    self.player_action = 'jump_loop'
                    self.player_frames = self.player.jump_loop(left=self.facing_left)
                elif self.player_action =='jump_loop':
                    self.player_action = 'jump_end'
                    self.player_frames = self.player.jump_end(left=self.facing_left)
                    self.GRAVITY = BASE_GRAVITY
            else:
                # we extend the frames in the jump function
                if not 'jump' in self.player_action:
                    self.curr_player_frame += 1
                
            if self.player_action == 'run_left':
                self.player.x -= self.player.MOVING_SPEED
            elif self.player_action == 'run_right':
                self.player.x += self.player.MOVING_SPEED
            elif 'jump' in self.player_action:
                self.jump()

            if self.player.x + self.player.SIZE >= self.WIDTH:
                self.player_action = 'idle'
                self.player_frames = self.player.idle()

            level.draw_ground()
            level.draw_platforms()
            self.SCREEN.blit(self.player_frames[self.curr_player_frame], (self.player.x, self.player.y))

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
