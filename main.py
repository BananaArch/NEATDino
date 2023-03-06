import pygame
from screen import *
from dinosaur import Dino
from background.ground import Ground
from background.clouds import Clouds

TPS = 600

def main():
    dino = Dino(100)
    ground = Ground()
    clouds = Clouds()
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

        vel = 10 + score / 100 if 10 + score / 100 < 15 else 15 # make nicer

        ground.vel = vel


        clouds.move()
        dino.move()
        ground.move()
        draw_screen(dino, ground, clouds)



    pygame.quit()
    quit()


main()
