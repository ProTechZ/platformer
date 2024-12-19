import pygame
import ctypes

from hand_detection import HandDetector

pygame.init()

user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screen = pygame.display.set_mode([0.5 * width, 0.6 * (height-60)])
# minus 60 to account for the title bar

model = HandDetector()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()
model.stop()