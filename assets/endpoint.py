import pygame
from os import getenv
from dotenv import load_dotenv

import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from utils import rescale_img

load_dotenv()

class EndPoint(pygame.sprite.Sprite):
    def __init__(self, SIZE, *groups):
        super().__init__(*groups)
        self.SIZE = SIZE

        self.close()
        self.rect = self.image.get_rect() 

    def close(self):
        base = getenv('BASE')
        closed = pygame.image.load(f"{base}\\platformer\\resources\\closed.png").convert()

        self.image = rescale_img(closed, self.SIZE)
    
    def open(self):
        base = getenv('BASE')
        open = pygame.image.load(f"{base}\\platformer\\resources\\open.png").convert()

        self.image = rescale_img(open, self.SIZE)

        