import pygame
from screen import *
from dinosaur import Dino
from obstacles.obstacles import Obstacles
from background.ground import Ground
from background.clouds import Clouds

TPS = 60

# stuff to implement
# score
# death screen
# start screen

def main():
    dino = Dino(100)
    ground = Ground()
    clouds = Clouds()
    obstacles = Obstacles()
    score = 0

    clock = pygame.time.Clock()
    delta = 0

    run = True
    while run:

        delta = clock.tick(TPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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

        obstacles.update_obstacles()

        # change vel
        # vel = 10 + score / 100 if 10 + score / 100 < 15 else 15 # make nicer
        vel = 10 * delta * TPS / 1000

        ground.vel = vel
        obstacles.vel = vel
        clouds.vel = vel / 10

        obstacles.move()
        clouds.move()
        dino.move()
        ground.move()
        draw_screen(dino, ground, clouds, obstacles)

        run = not obstacles.has_collided(dino)

    main()


main()
