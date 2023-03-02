import pygame
from screen import *
from dinosaur import Dino
from background.ground import Ground
from background.clouds import Clouds

TPS = 60

def main():
    dino = Dino(100)
    ground = Ground()
    cloud = Clouds()

    clock = pygame.time.Clock()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.set_is_jumping(True)
                if event.key == pygame.K_DOWN:
                   dino.set_is_ducking(True)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.set_is_jumping(False)
                if event.key == pygame.K_DOWN:
                    dino.set_is_ducking(False)

        cloud.move()
        dino.move()
        ground.move()
        draw_screen(dino, ground, cloud)

        clock.tick(TPS)

    pygame.quit()
    quit()


main()
