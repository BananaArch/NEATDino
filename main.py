import pygame
import random
from screen import *
from dinosaur import Dino
from obstacles.cactus import Cactus
from obstacles.bird import Bird
from background.ground import Ground
from background.clouds import Clouds

TPS = 60

def main():
    dino = Dino(100)
    ground = Ground()
    clouds = Clouds()
    obstacles = []
    score = 0

    clock = pygame.time.Clock()

    run = True
    while run:

        clock.tick(TPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.is_jumping = True
                if event.key == pygame.K_DOWN:
                   dino.is_ducking = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.is_jumping = False
                if event.key == pygame.K_DOWN:
                    dino.is_ducking = False

        # add obstacles
        # if something something
        obstacles.append(Cactus()) if random.choice([True, False]) else obstacles.append(Bird())


        # change vel
        vel = 10 + score / 100 if 10 + score / 100 < 15 else 15 # make nicer

        ground.vel = vel

        for obstacle in obstacles:
            obstacle.vel = vel
            obstacle.move()


        clouds.move()
        dino.move()
        ground.move()
        draw_screen(dino, ground, clouds, obstacles)



    pygame.quit()
    quit()


main()
