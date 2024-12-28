import pygame

from hand_detection import HandDetectorWindow
from assets.level import Level1
from assets.player import Player
from assets.platform import Platform

pygame.init()

class Game:
    def __init__(self, width, height):
        self.WIDTH = int(width)
        self.HEIGHT = int(height)
        self.SCREEN = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.CAMERA = HandDetectorWindow()

        self.is_running = True

        self.levels = [Level1(self.SCREEN)]
        self.curr_level_ind = 0

        self.player = Player(self.SCREEN, 100)

        self.player_action = 'idle'
        self.player_frames = self.player.idle()
        self.curr_player_frame = 0

    def run(self):
        while self.is_running:
            curr_level = self.levels[self.curr_level_ind]

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
                    if event.key == pygame.K_RIGHT:
                        if self.player_action == 'idle' or self.player_action == 'run_left':
                            self.player_frames = self.player.run_right()
                            self.player_action = 'run_right'
                    if event.key == pygame.K_SPACE:
                        if not self.player_action in ['jump_start', 'jump_loop', 'jump_end']:
                            self.player_frames = self.player.jump_start()
                            self.player_action = 'jump_start'           

            self.SCREEN.fill((255, 255, 255))
            camera, movement = self.CAMERA.start()
                                                                                                                                                                                                                                                                                        
            if camera is None:
                self.is_running = False
            else:       
                self.SCREEN.blit(camera, (0, 0))

            # resets the frame count if it reaches the end of the animation
            if self.curr_player_frame >= len(self.player_frames) - 1:
                self.curr_player_frame = 0

                if self.player_action == 'jump_start':
                    self.player_frames = self.player.jump_loop()
                    self.player_action = 'jump_loop'
                elif self.player_action == 'jump_loop':
                    self.player_frames = self.player.jump_end()
                    self.player_action = 'jump_end'
                elif self.player_action == 'jump_end':
                    self.player_frames = self.player.idle()
                    self.player_action = 'idle'

            else:
                self.curr_player_frame += 1
                if self.player_action == 'jump_loop':
                    self.player.jump()
                if self.player_action == 'jump_end':
                    self.player.fall()

            # the 2nd statements are checking if the player will touch the border on its next movement
            if self.player_action == 'run_left' and not self.player.x + 25 <= 0:
                self.player.x -= self.player.MOVING_SPEED
            elif self.player_action == 'run_right' and not self.player.x + self.player.SIZE - 25 >= self.WIDTH:
                self.player.x += self.player.MOVING_SPEED

            curr_level.draw_ground()
            curr_level.draw_platforms()
            self.SCREEN.blit(self.player_frames[self.curr_player_frame], (self.player.x, self.player.y))

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
