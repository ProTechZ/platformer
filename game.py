import pygame

from hand_detection import HandDetectorWindow
from assets.level import Level1
from assets.player import Player

pygame.init()

class Game:
    def __init__(self, width, height):
        self.WIDTH = int(width)
        self.HEIGHT = int(height)
        self.SCREEN = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.CAMERA = HandDetectorWindow()

        self.is_running = True

        self.levels = [Level1(self.SCREEN)]
        self.curr_level = 0

        self.player = Player(self.SCREEN, 100)
        self.player_x = 20
        self.player_y = 510
        self.speed = 4

        self.player_action = 'idle'
        self.player_frames = self.player.idle()
        self.curr_player_frame = 0

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.is_running=False 
                    if event.key == pygame.K_LEFT:
                        if not self.player_action == 'run_left':
                            self.player_frames = self.player.run_left()
                            self.curr_player_frame = 0
                            self.player_action = 'run_left'
                    if event.key == pygame.K_RIGHT:
                        if not self.player_action == 'run_right':
                            self.player_frames = self.player.run_right()
                            self.curr_player_frame = 0
                            self.player_action = 'run_right'
      
            self.SCREEN.fill((255, 255, 255))

            camera, movement = self.CAMERA.start()
                                                                                                                                                                                                                                                                                        
            if camera is None:
                self.is_running = False
            else:       
                self.SCREEN.blit(camera, (0, 0))

            # resets the frame count if it reaches the end of the animation
            if self.curr_player_frame >= len(self.player_frames) - 1:
                self.curr_player_frame = 0
            else:
                self.curr_player_frame += 1

            # the 2nd statements are checking if the player will touch the border on its next movement
            if self.player_action == 'run_left' and not self.player_x - self.speed <= 0:
                self.player_x -= self.speed
            elif self.player_action == 'run_right' and not self.player_x + self.player.SIZE + self.speed >= self.WIDTH:
                self.player_x += self.speed

            self.levels[self.curr_level].draw_ground()
            self.SCREEN.blit(self.player_frames[self.curr_player_frame], (self.player_x, self.player_y))

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
