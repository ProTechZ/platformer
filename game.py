import pygame

from hand_detection import HandDetectorWindow
from assets.level import Level1
from assets.player import Player
from assets.platform import Platform
from constants import *

pygame.init()

class Game:
    def __init__(self, width, height):
        self.WIDTH = int(width)
        self.HEIGHT = int(height)
        self.SCREEN = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        
        self.CLOCK = pygame.time.Clock()
        self.frame_counter = 0
        self.FRAME_DELAY = 5

        self.CAMERA = HandDetectorWindow()

        self.is_running = True

        self.levels = [Level1(self.SCREEN)]
        self.curr_level_ind = 0

        self.player = Player(self.SCREEN, PLAYER_WIDTH)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.is_running=False

                if event.key == pygame.K_LEFT:
                    if self.player.action in ['idle', 'run_right']:
                        self.player.set_run_left()

                if event.key == pygame.K_RIGHT:
                    if self.player.action in ['idle', 'run_left']:
                        self.player.set_run_right()

                if event.key == pygame.K_SPACE:
                    if not 'jump' in self.player.action:
                        self.player.set_jump_start()

    def touching_rborder(self):
        return self.player.x + self.player.SIZE - 25 >= self.WIDTH
    
    def touching_lborder(self):
        return self.player.x + 25 <= 0

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
            self.player.curr_frame += 1
            self.frame_counter = 0

    def run(self):
        while self.is_running:
            self.CLOCK.tick(FPS)
            self.event_loop()
            self.SCREEN.fill((255, 255, 255))

            movement = self.camera()
            level = self.levels[self.curr_level_ind]

            pygame.draw.rect(self.SCREEN, (0, 0, 0), self.player.rect, 1)

            # resets the frame count if it reaches the end of the animation
            if self.player.curr_frame >= len(self.player.frames) - 1:
                self.player.curr_frame = 0
                
                if self.player.action == 'jump_start':
                    self.player.set_jump_loop()
                elif self.player.action =='jump_loop':
                    self.player.set_jump_end()
            else:
                # because we are already extending the frames in the jump function
                if not 'jump' in self.player.action:
                    self.player.curr_frame += 1
                
            if self.player.action == 'run_left' and not self.touching_lborder():
                self.player.run_left()
            elif self.player.action == 'run_right' and not self.touching_rborder():
                self.player.run_right()
            elif 'jump' in self.player.action:
                self.player.jump(self.extend_frames)

            colliding_platforms = pygame.sprite.spritecollide(self.player, level.platforms, False)
            for platform in colliding_platforms:
                print(f'collide at {platform.rect.x}, {platform.rect.y}')

            level.draw_ground()
            level.platforms.update()
            level.platforms.draw(self.SCREEN)
            self.SCREEN.blit(self.player.image, (self.player.x, self.player.y))

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
