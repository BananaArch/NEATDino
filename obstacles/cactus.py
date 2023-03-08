import pygame
from sprites import *
from screen import SCREEN_WIDTH, SCREEN_HEIGHT
import random

CACTI_IMGS = [CACTUS_IMG,
              CACTUS_DOUBLE_A_IMG,
              CACTUS_DOUBLE_B_IMG,
              CACTUS_TRIPLE_IMG]
class Cactus:

    def __init__(self):
        self.img = CACTI_IMGS[random.randrange(0, len(CACTI_IMGS))]
        self.x = SCREEN_WIDTH
        self.y = .9 * SCREEN_HEIGHT - self.img.get_height()
        self.passed = False

    def move(self, vel):
        self.x -= vel
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
