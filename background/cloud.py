import pygame
import random
from screen import SCREEN_WIDTH, SCREEN_HEIGHT
from sprites import *

CLOUD_IMGS = [CLOUD_IMG, pygame.transform.flip(CLOUD_IMG, flip_x=True, flip_y=False)]
class Cloud:

    VEL = 1

    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = random.randrange(0, .4 * SCREEN_HEIGHT)
        self.img = CLOUD_IMGS[random.randrange(0, len(CLOUD_IMGS))]

    def move(self):
        self.x -= self.VEL

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
