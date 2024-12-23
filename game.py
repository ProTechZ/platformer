import pygame

from hand_detection import HandDetectorWindow
from level import Level1
from player import Player

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

        self.player_x = 20
        self.player_y = 400
        self.player = Player(self.SCREEN, 100, self.player_x, self.player_y)
        self.speed = 4

        self.player_frames_id = 'idle'
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
                        if not self.player_frames_id == 'run_left':
                            self.player_frames = self.player.run_left()
                            self.curr_player_frame = 0
                            self.player_frames_id = 'run_left'
                    if event.key == pygame.K_RIGHT:
                        if not self.player_frames_id == 'run_right':
                            self.player_frames = self.player.run_right()
                            self.curr_player_frame = 0
                            self.player_frames_id = 'run_right'
      
            self.SCREEN.fill((255, 255, 255))  
            frame, movement = self.CAMERA.start()

            if frame is None:
                self.is_running = False
            else:       
                self.SCREEN.blit(frame, (0, 0))

            if self.curr_player_frame >= len(self.player_frames) - 1:
                self.curr_player_frame = 0
            else:
                self.curr_player_frame += 1

            if self.player_frames_id == 'run_left':
                self.player_x -= self.speed
            if self.player_frames_id == 'run_right':
                self.player_x += self.speed

            self.levels[self.curr_level].draw_ground()
            self.SCREEN.blit(self.player_frames[self.curr_player_frame], (self.player_x, self.player_y))

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
