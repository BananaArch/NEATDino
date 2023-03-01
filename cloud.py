import pygame
import random
from screen import SCREEN_WIDTH, SCREEN_HEIGHT
from sprites import *


class Cloud:
    VEL = 1

    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = random.randrange(0, SCREEN_HEIGHT / 2)

    def move(self):
        self.x -= self.VEL

    def draw(self, screen):
        screen.blit(CLOUD_IMG, (self.x, self.y))


class Clouds:
    INCREASE_IN_PERCENT_CHANCE_PER_TICK = .1 / 60

    def __init__(self):
        self.clouds = []
        self.cloud_chance = 0
        self.cloud_threshold = 0

    def create_cloud(self):

        self.cloud_chance += self.INCREASE_IN_PERCENT_CHANCE_PER_TICK

        if self.cloud_threshold <= self.cloud_chance:
            self.clouds.append(Cloud())
            self.cloud_chance = random.uniform(0, self.cloud_threshold)
            self.cloud_threshold = random.random()

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

    def move(self):
        self.create_cloud()
        for cloud in self.clouds:
            cloud.move()