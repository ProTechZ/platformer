import pygame
import ctypes

from hand_detection import HandDetectorWindow

pygame.init()

user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 60
# minus 60 to account for the title bar

screen = pygame.display.set_mode([0.5 * width, 0.6 * height])

model = HandDetectorWindow(width=0.2 * width, height=0.2 * height)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running=False

    screen.fill((255, 255, 255))

    frame = model.run()
    
    if frame is None:
        running = False
    else:
        screen.blit(frame, (0, 0))

    pygame.display.flip()

pygame.quit()
model.stop()