import pygame

from hand_detection import HandDetectorWindow
from assets.level import Level1
from assets.player import Player
from assets.platform import Platform
from constants import FPS, BASE_GRAVITY, GROUND_LEVEL

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
                if event.key == pygame.K_RIGHT:
                    if self.player_action == 'idle' or self.player_action == 'run_left':
                        self.player_frames = self.player.run_right()
                        self.player_action = 'run_right'
                if event.key == pygame.K_SPACE:
                    if not 'jump' in self.player_action:
                        self.player_action = 'jump_start'
                        self.player.velocity_y = self.player.jump_force
                        self.player.velocity_x = self.player.jump_force
                        self.player_frames = self.player.jump_start()
                        self.curr_player_frame = 0

    def camera(self):
        camera, movement = self.CAMERA.start()
                                                                                                                                                                                                                                                                                        
        if camera is None:
            self.is_running = False
        else:       
            self.SCREEN.blit(camera, (0, 0))
            return movement
                                                                                                                                                                                                                                                                         
    def run(self):
        while self.is_running:
            self.CLOCK.tick(FPS)
            self.event_loop()

            movement = self.camera()
            level = self.levels[self.curr_level_ind]

            self.SCREEN.fill((255, 255, 255))

            #resets the frame count if it reaches the end of the animation
            if self.curr_player_frame >= len(self.player_frames) - 1:
                self.curr_player_frame = 0
                
                if self.player_action == 'jump_start':
                    self.player_action = 'jump_loop'
                    self.player_frames = self.player.jump_loop()
                elif self.player_action =='jump_loop':
                    self.player_action = 'jump_end'
                    self.player_frames = self.player.jump_end()
                    self.GRAVITY = BASE_GRAVITY
            else:
                if not 'jump' in self.player_action:
                    self.curr_player_frame += 1

            pygame.draw.rect(self.SCREEN, (255, 0, 0), (0, self.player.y, self.WIDTH, 1))
            pygame.draw.circle(self.SCREEN, (0, 0, 0), (self.player.x, self.player.y), 5)

            if 'jump' in self.player_action:

                self.frame_counter += 1
                if self.frame_counter >= self.FRAME_DELAY:
                    self.curr_player_frame += 1
                    self.frame_counter = 0

                if self.player_action == 'jump_start' or self.player_action == 'jump_loop':
                    self.player.velocity_y -= self.GRAVITY
                    self.GRAVITY += 0.01
                    self.player.y -= self.player.velocity_y
                elif self.player_action == 'jump_end':
                    self.player.velocity_y += self.GRAVITY
                    self.GRAVITY += 0.01
                    self.player.y += self.player.velocity_y

                self.player.x += self.player.velocity_x

                if self.player.y >= GROUND_LEVEL + 5:
                    self.player.y = GROUND_LEVEL
                    self.player.velocity_y = 0
                    self.player.velocity_x = 0
                    self.curr_player_frame = 0
                    self.player_frames = self.player.idle()
                    self.player_action = 'idle'
                    self.GRAVITY = BASE_GRAVITY
            
            # the 2nd statements are checking if the player will touch the border on its next movement
            if self.player_action == 'run_left' and not self.player.x + 25 <= 0:
                self.player.x -= self.player.MOVING_SPEED
            elif self.player_action == 'run_right' and not self.player.x + self.player.SIZE - 25 >= self.WIDTH:
                self.player.x += self.player.MOVING_SPEED

            level.draw_ground()
            level.draw_platforms()
            self.SCREEN.blit(self.player_frames[self.curr_player_frame], (self.player.x, self.player.y))

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
