# AI Platformer

This is a platfomer game made with pygame where you control the player with your hand gestures. The hand gestures are tracked by MediaPipe.

![giphy](https://github.com/user-attachments/assets/454bcdd1-6843-4378-80c8-8a1a68da3ab8)

## Playing the Game
The aim of the game is to reach the gate on the last platform. Once you reach the last platform, the gate will open and you can go through to the next level.

You control the player by using hand gestures. Moving your hand left and right moves the player in that respective direction. To jump, you move your hand upwards. The jump detection threshold is a bit high to account for the fact that your hand will always be moving slightly upwards.

I recommend placing your hand at the far left side of the camera when playing so that you have the entire camera length to move your hand sideways and up.

There are 3 default levels but you can always add more levels. Skip to [Level Making](#level-making) to see how to.

## Tech Stack
 - Python
 - Pygame - for the game making
 - Mediapipe - for the hand gesture recognition
   
   `mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)`

## Setup

To use and try out the project for yourself, follow these steps.

1. Clone the repository:

   ```bash
   git clone https://github.com/ProTechZ/platformer.git
   cd platformer
   ```

2. Install the required libraries
 
   ```bash
   pip install -r requirements.txt
   ```

3. Add environment variables.

   Create a file named `.env`, create a variable named `BASE` and set it to the folder path before the project. For example, if the project folder path is `C:\Users\zion\Desktop\platformer\`, the `.env` file should look like this:

   ```
   BASE=C:\Users\zion\Desktop\
   ```

4. Run main.py.

   ```bash
   python main.py
   ```

## Level Making
To add your own custom levels, go to the `all_levels.py` file, and paste this code:

```py
class Level4(Level):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        platforms_details = [
          # add platforms here
        ]

        self.gen_platforms(platforms_details)
```

Change the level name to whatever you want. To add a platform, you just need to add a tuple to the `platform_details` list. The tuple should look like `(x, y, width, height)`.

After you've finished adding your levels, go the `game.py` file and scroll to the `__init__` function. Go to the `self.levels` property and add your level there. For example, if you named your new level Level4, add `Level4(self.SCREEN, self.player)` to the list.
