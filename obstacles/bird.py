import pygame
from sprites import *
from screen import SCREEN_HEIGHT, SCREEN_WIDTH

BIRD_IMGS = [BIRD_UP_IMG, BIRD_DOWN_IMG]
class Bird:

    VEL = 1
    ANIMATION_SPEED = 5

    def __init__(self):
        self.img = BIRD_IMGS[0]
        self.x = SCREEN_WIDTH
        self.y = .9 * SCREEN_HEIGHT - self.img.get_height()
        self.img_count = 0

    def move(self):
        self.x -= self.VEL

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))



