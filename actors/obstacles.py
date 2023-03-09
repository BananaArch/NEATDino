import pygame
import random
from game.screen import SCREEN_WIDTH
from actors.bird import Bird
from actors.cactus import Cactus


class Obstacles:

    def __init__(self):
        self.obstacles = [Cactus()]
        self.x_threshold = 0 * SCREEN_WIDTH

    def update_obstacles(self):

        for obstacle in self.obstacles:
            if not obstacle.passed and obstacle.x < self.x_threshold:
                obstacle.passed = True
                self.obstacles.append(random.choice([Cactus(), Cactus(), Bird()]))
                self.x_threshold = random.uniform(.3 * SCREEN_WIDTH, .45 * SCREEN_WIDTH)

            if obstacle.x < -obstacle.img.get_width():
                self.obstacles.remove(obstacle)

    def move(self, vel):
        for obstacle in self.obstacles:
            obstacle.move(vel)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def has_collided(self, dino):

        dino_run_mask = pygame.mask.from_surface(dino.img)

        for obstacle in self.obstacles:

            obstacle_mask = pygame.mask.from_surface(obstacle.img)
            obstacle_x_offset = dino.x + dino.img.get_width() - (obstacle.x + obstacle.img.get_width())
            obstacle_y_offset = dino.y + dino.img.get_height() - (obstacle.y + obstacle.img.get_height())

            if dino_run_mask.overlap(obstacle_mask, (obstacle_x_offset, obstacle_y_offset)):
                return True

        return False
