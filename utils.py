import pygame
from PIL import Image

def flip_frames(frames):
    return [pygame.transform.flip(frame, True, False) for frame in frames]

def rescale_img(img, size):
    width = int(img.get_width())
    height = int(img.get_height())
    scale = size/width

    return pygame.transform.scale(img, (size, height * scale))

def pil_to_pygame(img):
    return pygame.image.fromstring(
        img.tobytes(), img.size, "RGBA"
    )

def get_bigget_bbox(img_list):
    x1_min, y1_min, x2_max, y2_max = float('inf'), float('inf'), float('-inf'), float('-inf')

    for frame in img_list:
        bbox = frame.getbbox()
        if bbox:
            x1, y1, x2, y2 = bbox
            x1_min = min(x1_min, x1)
            y1_min = min(y1_min, y1)
            x2_max = max(x2_max, x2)
            y2_max = max(y2_max, y2)
    
    return (x1_min, y1_min, x2_max, y2_max)
