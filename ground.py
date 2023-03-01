from sprites import *
from screen import SCREEN_HEIGHT

GROUND_IMG = GROUND_IMG

class Ground:

    VEL = 10
    # 10-15
    WIDTH = GROUND_IMG.get_width()
    HEIGHT = .9 * SCREEN_HEIGHT - GROUND_IMG.get_height()
    # HEIGHT WILL BE AT 90% of SCREEN_HEIGHT
    IMG = GROUND_IMG

    def __init__(self):
        self.y = self.HEIGHT
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 < 0:
            self.x2 = self.WIDTH + self.x1

        if self.x2 < 0:
            self.x1 = self.WIDTH + self.x2

    def draw(self, screen):
        screen.blit(self.IMG, (self.x1, self.y))
        screen.blit(self.IMG, (self.x2, self.y))