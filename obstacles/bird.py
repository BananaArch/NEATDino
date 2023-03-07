import pygame
import random
from sprites import *
from screen import SCREEN_HEIGHT, SCREEN_WIDTH

BIRD_IMGS = [BIRD_UP_IMG, BIRD_DOWN_IMG]
class Bird:

    ANIMATION_SPEED = 5

    POSSIBLE_Y = [.9 * SCREEN_HEIGHT - 2.6 * BIRD_IMGS[0].get_height(),
                  .9 * SCREEN_HEIGHT - 1.6 * BIRD_IMGS[0].get_height()]

    def __init__(self):
        self.img = BIRD_IMGS[0]
        self.x = SCREEN_WIDTH
        self.y = random.choice(self.POSSIBLE_Y)
        self.img_count = 0
        self.vel = 10
        self.passed = False

    def move(self):
        self.x -= self.vel

        self.img_count += 1
        self.img = BIRD_IMGS[self.img_count // self.ANIMATION_SPEED % len(BIRD_IMGS)]

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
