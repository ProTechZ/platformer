import pygame

def flip_frames(frames):
    return [pygame.transform.flip(frame, True, False) for frame in frames]

def rescale_img(img, size):
    width = int(img.get_width())
    height = int(img.get_height())
    scale = size/width

    return pygame.transform.scale(img, (size, height * scale))