import math
import pygame
from pygame import mixer
from game.screen import *
from game.sfx import *
from actors.dinosaur import Dino
from actors.obstacles import Obstacles
from background.ground import Ground
from background.clouds import Clouds
from game.start_menu import start_menu
from game.death_menu import death_menu

TPS = 60


# stuff to implement

# NEAT
# round() == smoother?

def main():
    dino = Dino(100)
    ground = Ground()
    clouds = Clouds()
    obstacles = Obstacles()
    vel = 10
    score = 0

    start_menu(dino, ground, clouds, obstacles)

    clock = pygame.time.Clock()

    run = True
    while run:

        dt = clock.tick(TPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.is_jumping = True
                    if dino.y is dino.min_height:
                        play_player_action()
                if event.key == pygame.K_DOWN:
                    dino.is_ducking = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.is_jumping = False
                if event.key == pygame.K_DOWN:
                    dino.is_ducking = False

        obstacles.update_obstacles()

        dino.move()
        obstacles.move(vel * dt * TPS / 1000)
        ground.move(vel * dt * TPS / 1000)
        clouds.move((vel * dt * TPS / 1000) / 10)

        draw_screen(dino, ground, clouds, obstacles, score)
        pygame.display.update()

        if obstacles.has_collided(dino):
            run = False

        score += .05 + score / 2000

        vel = vel + .002 if vel < 25 else 25

        # goes 100, 200, 300 ... , 1000, 2000, 3000 ...
        if round(score) % math.pow(10, math.floor(math.log10(score))) == 0 and score >= 100:
            play_achievement()

    play_gameover()
    death_menu()
    main()


main()
