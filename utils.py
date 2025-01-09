import pygame
from PIL import Image

def flip_frames(frames):
    return [pygame.transform.flip(frame, True, False) for frame in frames]

def rescale_img(img, size):
    width = int(img.get_width())
    height = int(img.get_height())
    scale = size/width

    return pygame.transform.scale(img, (size, height * scale))

def crop_pygame_transparent(img):
    # convert to PIL format
    raw_data = pygame.image.tobytes(img, "RGBA")
    pil_image = Image.frombytes("RGBA", img.get_size(), raw_data)

    bbox = pil_image.getbbox()
    if not bbox:
        return img

    # crop the image and convert it back to a Pygame surface
    cropped_pil = pil_image.crop(bbox)
    cropped_surface = pygame.image.fromstring(
        cropped_pil.tobytes(), cropped_pil.size, "RGBA"
    )

    return cropped_surface
