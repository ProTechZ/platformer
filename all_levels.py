from assets.level import Level

class Level1(Level):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        platforms_details = [
            (220, 475, 200, 50),
            (450, 400, 200, 50),
            (700, 325, 200, 50),
        ]

        self.gen_platforms(platforms_details)

class Level2(Level):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        platforms_details = [
            (100, 525, 200, 40),
            (400, 475, 200, 50),
            (600, 425, 250, 40),
            (325, 300, 200, 40),
        ]   

        self.gen_platforms(platforms_details)

class Level3(Level):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        platforms_details = [
            (100, 525, 200, 40),
            (400, 450, 200, 50),
            (750, 400, 200, 40),
        ]

        self.gen_platforms(platforms_details)