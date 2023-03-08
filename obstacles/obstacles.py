import pygame
import random
from screen import SCREEN_WIDTH
from obstacles.bird import Bird
from obstacles.cactus import Cactus


class Obstacles:

    def __init__(self):
        self.obstacles = [Cactus()]
        self.x_threshold = random.uniform(.4 * SCREEN_WIDTH, .6 * SCREEN_WIDTH)

    def update_obstacles(self):

        for obstacle in self.obstacles:
            if not obstacle.passed and obstacle.x < self.x_threshold:
                obstacle.passed = True
                self.obstacles.append(random.choice([Cactus(), Cactus(), Bird()]))
                self.x_threshold = random.uniform(0 * SCREEN_WIDTH, .5 * SCREEN_WIDTH)

            if obstacle.x < -obstacle.img.get_width():
                self.obstacles.remove(obstacle)

    def move(self, vel):
        for obstacle in self.obstacles:
            obstacle.move(vel)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def has_collided(self, dino):

        dino_mask = dino.get_mask()

        for obstacle in self.obstacles:

            obstacle_mask = obstacle.get_mask()
            obstacle_offset = (dino.x - obstacle.x, obstacle.y - round(dino.y))

            if dino_mask.overlap(obstacle_mask, obstacle_offset):
                return True

        return False
