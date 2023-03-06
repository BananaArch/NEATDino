import pygame
from sprites import *
from screen import SCREEN_HEIGHT, SCREEN_WIDTH

BIRD_IMGS = [BIRD_UP_IMG, BIRD_DOWN_IMG]
class Bird:

    ANIMATION_SPEED = 5

    def __init__(self):
        self.img = BIRD_IMGS[0]
        self.x = SCREEN_WIDTH
        self.y = .9 * SCREEN_HEIGHT - self.img.get_height()
        self.img_count = 0
        self.vel = 10

    def move(self):
        self.x -= self.vel

        self.img_count += 1
        self.img = BIRD_IMGS[self.img_count // self.ANIMATION_SPEED % len(BIRD_IMGS)]

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

# TODO: ADD MASKING