class Obstacles:

    obstacles = []

    def __init__(self):
        self.obstacles = []
        self.vel = self.VEL_INITIAL

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw()
