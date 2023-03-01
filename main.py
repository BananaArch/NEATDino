import pygame
from screen import *
from dinosaur import Dino
from ground import Ground

TPS = 60

def main():
    dino = Dino(100)
    ground = Ground()

    clock = pygame.time.Clock()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dino.set_is_jumping(True)
                if event.key == pygame.K_DOWN:
                    dino.set_is_ducking(True)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    dino.set_is_jumping(False)
                if event.key == pygame.K_DOWN:
                    dino.set_is_ducking(False)


        dino.move()
        ground.move()
        draw_screen(dino, ground)

        clock.tick(TPS)

    pygame.quit()
    quit()


main()
