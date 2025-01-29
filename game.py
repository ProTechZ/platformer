import pygame

from hand_detection import HandDetectorWindow
from assets.level import Level1
from assets.player import Player
from constants import PLAYER_WIDTH, GROUND_LEVEL

pygame.init()

class Game:
    def __init__(self, width, height):
        self.WIDTH = int(width)
        self.HEIGHT = int(height)
        self.SCREEN = pygame.display.set_mode([self.WIDTH, self.HEIGHT])

        self.CLOCK = pygame.time.Clock()
        self.FPS = 30

        self.CAMERA = HandDetectorWindow()

        self.is_running = True

        self.player = Player(self.SCREEN, PLAYER_WIDTH)
        self.levels = [Level1(self.SCREEN, self.player)]
        self.curr_level_ind = 0

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

                if event.key == pygame.K_DOWN:
                    self.player.set_idle()

                if event.key == pygame.K_SPACE:
                    if not 'jump' in self.player.action:
                        self.player.set_jump_start()
    
    def border_collision(self):
        if self.player.x + self.player.SIZE >= self.WIDTH or self.player.x <= 0:
            self.player.move_while_running = False

    def camera(self):
        camera, movement = self.CAMERA.start()
                                                        
        if camera is None:
            self.is_running = False
        else:
            self.SCREEN.blit(camera, (0, 0))
            return movement

    def run(self):
        while self.is_running:
            self.CLOCK.tick(self.FPS)
            self.event_loop()
            self.SCREEN.fill((255, 255, 255))

            movement = self.camera()
            level = self.levels[self.curr_level_ind]

            pygame.draw.rect(self.SCREEN, (0, 0, 0), (self.player.x, self.player.y, self.player.SIZE, self.player.image.get_height()), 1)

            # resets the frame count if it reaches the end of the animation
            if self.player.curr_frame >= len(self.player.frames) - 1:
                self.player.curr_frame = 0

                if self.player.action == 'jump_start':
                    self.player.set_jump_loop()
                elif self.player.action =='jump_loop':
                    self.player.set_jump_end()
                elif self.player.action == 'jump_end' and self.player.y >= GROUND_LEVEL:
                    self.player.set_idle()
            else:
                self.player.curr_frame += 1

            for platform in level.platforms:
                level.detect_collision(self.player, platform)

            if self.player.action == 'run_left':
                self.player.run_left()
            elif self.player.action == 'run_right':
                self.player.run_right()
            elif 'jump' in self.player.action:
                self.player.jump()

            level.draw_ground()
            level.platforms.update()
            level.platforms.draw(self.SCREEN)
            
            self.SCREEN.blit(self.player.image, (self.player.x, self.player.y))
            self.border_collision()

            pygame.display.flip()

        pygame.quit()
        self.CAMERA.stop()
