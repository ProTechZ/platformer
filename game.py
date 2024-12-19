import pygame
import ctypes

from hand_detection import HandDetectorWindow

pygame.init()

user32 = ctypes.windll.user32
win_width, win_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 60
# minus 60 to account for the title bar

WIDTH = 0.5 * win_width
HEIGHT = 0.6 * win_height
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])

model = HandDetectorWindow(width=0.4 * WIDTH, height=0.4 * HEIGHT)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running=False

    SCREEN.fill((255, 255, 255))

    frame = model.run()
    
    if frame is None:
        running = False
    else:
        SCREEN.blit(frame, (0, 0))

    pygame.display.flip()

pygame.quit()
model.stop()