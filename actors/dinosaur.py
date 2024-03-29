import pygame

from game.sprites import *
from game.screen import SCREEN_HEIGHT
from game.sfx import play_player_action

STILL_IMG = DINO_STILL_IMG
RUN_IMGS = [DINO_LEFT_IMG, DINO_RIGHT_IMG]
DUCK_IMGS = [DINO_DUCK_LEFT_IMG, DINO_DUCK_RIGHT_IMG]

class Dino:

    RUN_MIN_HEIGHT = .9 * SCREEN_HEIGHT - RUN_IMGS[0].get_height() # 90% OF SCREEN
    DUCK_MIN_HEIGHT = .9 * SCREEN_HEIGHT - DUCK_IMGS[0].get_height()
    GRAVITY_ACCELERATION = 1
    ANIMATION_TIME = 4

    def __init__(self, x):
        self.min_height = self.RUN_MIN_HEIGHT
        self.x = x
        self.y = self.RUN_MIN_HEIGHT
        self.vel = 0
        self.acc = self.GRAVITY_ACCELERATION
        self.tick_count = 0
        self.img_count = 0
        self.is_jumping = False
        self.is_ducking = False
        self.img = STILL_IMG
    def move(self):

        self.img_count += 1

        if self.is_ducking and not self.is_jumping:
            self.img = DUCK_IMGS[self.img_count // self.ANIMATION_TIME % len(DUCK_IMGS)]
            self.min_height = self.DUCK_MIN_HEIGHT
            self.acc *= 1.3
        elif self.is_jumping and not self.is_ducking or self.y < self.min_height:
            self.img = STILL_IMG
            self.min_height = self.RUN_MIN_HEIGHT
            self.acc = self.GRAVITY_ACCELERATION
        else:
            self.img = RUN_IMGS[self.img_count // self.ANIMATION_TIME % len(RUN_IMGS)]
            self.min_height = self.RUN_MIN_HEIGHT


        # jump
        if self.is_jumping and self.y is self.min_height:
            # initial velocity when jumping
            self.vel = - 18
            play_player_action()

        self.vel += self.acc


        if self.y + self.vel <= self.min_height:
            self.y += self.vel
        else:
            self.y = self.min_height


    def draw(self, screen):

        screen.blit(self.img, (self.x, self.y))

    def draw_alpha(self, screen):

        alpha = 255 // 2

        alpha_img = self.img.copy()
        alpha_img.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        screen.blit(alpha_img, (self.x, self.y))