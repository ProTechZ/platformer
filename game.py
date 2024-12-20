import pygame

from hand_detection import HandDetectorWindow

pygame.init()

class Game:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN = pygame.display.set_mode([width, height])

        self.CAMERA = HandDetectorWindow(width=0.4 * width, height=0.4 * height)

        self.is_running = True

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
                print(movement)

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
