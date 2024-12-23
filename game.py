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

        self.player = Player(screen=self.SCREEN, size=100)
        
    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.is_running=False 
      
            self.SCREEN.fill((255, 255, 255))  
            frame, movement = self.CAMERA.start()

            if frame is None:
                self.is_running = False
            else:       
                self.SCREEN.blit(frame, (0, 0))

            self.levels[self.curr_level].draw_ground()
            player = self.player.run_left()

            self.SCREEN.blit(player, (40, 200))

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
