import pygame
import random
from screen import SCREEN_WIDTH
from obstacles.bird import Bird
from obstacles.cactus import Cactus

class Obstacles:

    def __init__(self):
        self.obstacles = [Cactus()]
        self.vel = 10
        self.x_threshold = random.uniform(.3 * SCREEN_WIDTH, .5 * SCREEN_WIDTH)

    def update_obstacles(self):

        for obstacle in self.obstacles:
            if not obstacle.passed and obstacle.x < self.x_threshold:
                obstacle.passed = True
                self.obstacles.append(random.choice([Bird(), Cactus()]))
                self.x_threshold = random.uniform(0 * SCREEN_WIDTH, .5 * SCREEN_WIDTH)

            if obstacle.x < -obstacle.img.get_width():
                self.obstacles.remove(obstacle)

    def move(self):
        for obstacle in self.obstacles:
            obstacle.vel = self.vel
            obstacle.move()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)