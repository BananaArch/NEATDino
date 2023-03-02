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


class Clouds:

    INCREASE_IN_PERCENT_CHANCE_PER_TICK = .06 / 60

    def __init__(self):
        self.clouds = []
        self.cloud_chance_initial = 0
        self.cloud_chance = 0
        self.cloud_chance_final = 0

    def create_cloud(self):

        # TODO: Create better cloud-spawning algorithm

        self.cloud_chance += self.INCREASE_IN_PERCENT_CHANCE_PER_TICK

        # if increasing cloud_chance crosses threshold, spawns new cloud
        if self.cloud_chance >= self.cloud_chance_final:

            self.clouds.append(Cloud())
            cloud_chance_difference = self.cloud_chance_final - self.cloud_chance_initial
            self.cloud_chance_initial, self.cloud_chance_final = random.uniform(0, 1 - cloud_chance_difference), random.uniform(1 - cloud_chance_difference, 1)
            self.cloud_chance = self.cloud_chance_initial

            print(self.cloud_chance_initial)
            print(self.cloud_chance_final)
            print('\n')



    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

    def move(self):
        self.create_cloud()
        for cloud in self.clouds:
            cloud.move()