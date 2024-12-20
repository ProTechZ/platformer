import ctypes
from game import Game

user32 = ctypes.windll.user32
win_width, win_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 60
# minus 60 to account for the title bar

game = Game(0.5 * win_width, 0.6 * win_height)
game.run()