import pygame
import random
from screen import SCREEN_WIDTH
from obstacles.bird import Bird
from obstacles.cactus import Cactus
from sprites import DINO_STILL_IMG


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

        dino_run_mask = pygame.mask.from_surface(dino.RUN_IMGS[0])
        dino_duck_mask = pygame.mask.from_surface(dino.STILL_IMG)

        for obstacle in self.obstacles:

            obstacle_mask = pygame.mask.from_surface(obstacle.img)
            obstacle_offset = (dino.x - obstacle.x, dino.y - obstacle.y)
            # obstacle_offset = (dino.x - obstacle.x, obstacle.y - round(dino))
            # print('x ' + str(dino.x - obstacle.x))
            # print('y ' + str(obstacle.y - round(dino.y)))

            if dino_run_mask.overlap(obstacle_mask, obstacle_offset):
                print('collided')
                return True

        return False
