import pygame
from os import getenv
import cv2

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups, screen, size):
        super().__init__(*groups)

        self.idle_frame = 0
        self.running_frame = 0

        self.SCREEN = screen
        self.SIZE = size

    def rescale_player(self, player, size):
        width = int(player.get_width())
        height = int(player.get_height())
        scale = size/width
        
        return pygame.transform.scale(player, (size, height * scale))

    def idle(self):
        base = getenv('BASE')
        player  = pygame.image.load(f"{base}platformer\\images\\player assets\\Idle\\Player_Idle_{self.idle_frame}.png")
        
        if self.idle_frame == 17:
            self.idle_frame = 0
        else:
            self.idle_frame += 1

        return self.rescale_player(player, self.size)

    def run(self):
        base = getenv('BASE')
        player  = pygame.image.load(f"{base}platformer\\images\\player assets\\Running\\Player_Running_{self.running_frame}.png")
        
        if self.running_frame == 11:
            self.running_frame = 0
        else:
            self.running_frame += 1

        return self.rescale_player(player, self.size)


    