import pygame
from os import getenv
from utils import flip_frames, rescale_img

FPS = 60

BASE_GRAVITY = 0.1
GRAVITY_INCREMENT = 0.2
GRAVITY = BASE_GRAVITY

GROUND_LEVEL = 487
PLAYER_SIZE = 100

def idle(left=False):
    base = getenv('BASE')
    player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Idle\\Player_Idle_{i}.png") for i in range(18)]
   
    if left: 
        player_frames = flip_frames(player_frames)
   
    return [rescale_img(frame, PLAYER_SIZE) for frame in player_frames]

def run_right():
    base = getenv('BASE')
    player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Running\\Player_Running_{i}.png") for i in range(12)]
    return [rescale_img(frame, PLAYER_SIZE) for frame in player_frames]

def run_left():
    base = getenv('BASE')
    player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Running\\Player_Running_{i}.png") for i in range(12)]
    player_frames = flip_frames(player_frames)
    return [rescale_img(frame, PLAYER_SIZE) for frame in player_frames]

def jump_start(left=False):
    base = getenv('BASE')
    player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Jump Start\\Player_Jump_Start_{i}.png") for i in range(6)]
  
    if left: 
        player_frames = flip_frames(player_frames)
   
    return [rescale_img(frame, PLAYER_SIZE) for frame in player_frames]

def jump_loop(left=False):
    base = getenv('BASE')
    player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Jump Loop\\Player_Jump_Loop_{i}.png") for i in range(6)]
  
    if left: 
        player_frames = flip_frames(player_frames)
   
    return [rescale_img(frame, PLAYER_SIZE) for frame in player_frames]

def jump_end(left=False):
    base = getenv('BASE')
    player_frames  = [pygame.image.load(f"{base}platformer\\resources\\player assets\\Falling Down\\Player_Falling_Down_{i}.png") for i in range(6)]
    
    if left: 
        player_frames = flip_frames(player_frames)
   
    return [rescale_img(frame, PLAYER_SIZE) for frame in player_frames]