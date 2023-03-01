from sprites import *
from screen import SCREEN_HEIGHT

DINO_RUN_IMGS = [DINO_STILL_IMG, DINO_LEFT_IMG, DINO_RIGHT_IMG]
DINO_DUCK_IMGS = [DINO_DUCK_LEFT_IMG, DINO_DUCK_RIGHT_IMG]

class Dino:

    RUN_IMGS = DINO_RUN_IMGS
    DUCK_IMGS = DINO_DUCK_IMGS
    RUN_MIN_HEIGHT = .9 * SCREEN_HEIGHT - DINO_RUN_IMGS[0].get_height() # 90% OF SCREEN
    DUCK_MIN_HEIGHT = .9 * SCREEN_HEIGHT - DINO_DUCK_IMGS[0].get_height()
    GRAVITY_ACCELERATION = 1
    ANIMATION_TIME = 3

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
        self.img = self.RUN_IMGS[0]

    def set_is_jumping(self, boolean):
        self.is_jumping = boolean

    def set_is_ducking(self, boolean):
        self.is_ducking = boolean

    def move(self):

        self.img_count += 1

        if self.is_jumping and not self.is_ducking:
            self.img = self.RUN_IMGS[0]
            self.min_height = self.RUN_MIN_HEIGHT
            self.acc = self.GRAVITY_ACCELERATION
        elif self.is_ducking and not self.is_jumping:
            self.img = self.DUCK_IMGS[self.img_count // self.ANIMATION_TIME % len(self.DUCK_IMGS)]
            self.min_height = self.DUCK_MIN_HEIGHT
            self.acc *= 2
        else:
            self.img = self.RUN_IMGS[self.img_count // self.ANIMATION_TIME % len(self.RUN_IMGS)]
            self.min_height = self.RUN_MIN_HEIGHT


        # jump
        if self.is_jumping and self.y is self.min_height:
            # initial velocity when jumping
            self.vel = - 18

        self.vel += self.acc


        if self.y + self.vel <= self.min_height:
            self.y += self.vel
        else:
            self.y = self.min_height


    def draw(self, screen):

        screen.blit(self.img, (self.x, self.y))
        pass
