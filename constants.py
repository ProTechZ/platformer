import pygame
from os import getenv
from utils import flip_frames, rescale_img, pil_to_pygame, get_bigget_bbox
from PIL import Image

FPS = 60

BASE_GRAVITY = 0.1
GRAVITY_INCREMENT = 0.2
GRAVITY = BASE_GRAVITY

GROUND_LEVEL = 505 
PLAYER_WIDTH = 50

def get_frames(path, num_frames, left):
    base = getenv('BASE')

    player_frames = []
    mbbox = get_bigget_bbox([Image.open(f"{base}{path}{i}.png") for i in range(num_frames)])

    for i in range(num_frames):
        frame = Image.open(f"{base}{path}{i}.png")
        frame = frame.crop(mbbox)
        frame = pil_to_pygame(frame)
        frame = rescale_img(frame, PLAYER_WIDTH)
        player_frames.append(frame)

    if left:
        player_frames = flip_frames(player_frames)
    
    return player_frames

def idle(left=False):
    return get_frames("platformer\\resources\\player assets\\Idle\\Player_Idle_", 18, left)

def run(left=False):
    return get_frames("platformer\\resources\\player assets\\Running\\Player_Running_", 12, left)

def jump_start(left=False):
    return get_frames("platformer\\resources\\player assets\\Jump Start\\Player_Jump_Start_", 6, left)

def jump_loop(left=False):
    return get_frames("platformer\\resources\\player assets\\Jump Loop\\Player_Jump_Loop_", 6, left)

def jump_end(left=False):
    return get_frames("platformer\\resources\\player assets\\Falling Down\\Player_Falling_Down_", 6, left)
