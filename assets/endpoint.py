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

        self.image = self._generate()
        self.rect = self.image.get_rect() 

    def _generate(self):
        base = getenv('BASE')
        endpoint_img = pygame.image.load(f"{base}\\platformer\\resources\\endpoint.png").convert()

        return rescale_img(endpoint_img, self.SIZE)
        