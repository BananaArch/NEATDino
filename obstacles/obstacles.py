class Obstacles:

    VEL_INITIAL = 5
    VEL_FINAL = 10
    obstacles = []

    def __init__(self):
        self.obstacles = []
        self.vel = self.VEL_INITIAL

    def draw(self):

        