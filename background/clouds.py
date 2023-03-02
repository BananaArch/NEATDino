import pygame
from background.cloud import Cloud
import random

class Clouds:

    INCREASE_IN_PERCENT_CHANCE_PER_TICK = .06 / 60

    def __init__(self):
        self.clouds = []
        self.cloud_chance_initial = 0
        self.cloud_chance = 0
        self.cloud_chance_final = 0

    def create_cloud(self):

        self.cloud_chance += self.INCREASE_IN_PERCENT_CHANCE_PER_TICK

        # if increasing cloud_chance crosses threshold, spawns new cloud
        if self.cloud_chance >= self.cloud_chance_final:

            self.clouds.append(Cloud())
            cloud_chance_difference = self.cloud_chance_final - self.cloud_chance_initial
            self.cloud_chance_initial = random.uniform(0, cloud_chance_difference)
            self.cloud_chance_final = random.uniform(self.cloud_chance_initial, 1)
            self.cloud_chance = self.cloud_chance_initial

            # print(self.cloud_chance_initial)
            # print(self.cloud_chance_final)
            # print('\n')



    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

    def move(self):
        self.create_cloud()
        for cloud in self.clouds:
            cloud.move()