import random

class Level:
  def __init__(self):
    pass

  def gen_platforms_coords(self, num):
        coords = [
            (random.randrange(self.CAMERA.width, self.WIDTH), 
            random.randrange(self.CAMERA.height, self.HEIGHT)) 
            for _ in range(num)
        ]

        return coords