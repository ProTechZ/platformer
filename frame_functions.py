from os import getenv
from utils import flip_frames, rescale_img, pil_to_pygame, get_bigget_bbox
from PIL import Image
from constants import PLAYER_WIDTH

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

def get_idle_frames(left=False):
    return get_frames("platformer\\resources\\player assets\\Idle\\Player_Idle_", 18, left)

def get_run_frames(left=False):
    return get_frames("platformer\\resources\\player assets\\Running\\Player_Running_", 12, left)

def get_jump_start_frames(left=False):
    return get_frames("platformer\\resources\\player assets\\Jump Start\\Player_Jump_Start_", 6, left)

def get_jump_loop_frames(left=False):
    return get_frames("platformer\\resources\\player assets\\Jump Loop\\Player_Jump_Loop_", 6, left)

def get_jump_end_frames(left=False):
    return get_frames("platformer\\resources\\player assets\\Falling Down\\Player_Falling_Down_", 6, left)

idleR = get_idle_frames()
idleL = get_idle_frames(left=True)

runR = get_run_frames()
runL = get_run_frames(left=True)

jump_startR = get_jump_start_frames()
jump_startL = get_jump_start_frames(left=True)

jump_loopR = get_jump_loop_frames()
jump_loopL = get_jump_loop_frames(left=True)

jump_endR = get_jump_end_frames()
jump_endL = get_jump_end_frames(left=True)

def idle(left=False):
    return idleL if left else idleR

def run(left=False):
    return runL if left else runR

def jump_start(left=False):
    return jump_startL if left else jump_startR

def jump_loop(left=False):
    return jump_loopL if left else jump_loopR

def jump_end(left=False):
    return jump_endL if left else jump_endR