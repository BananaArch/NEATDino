import pygame
from screen import *

def death_menu(dino, ground, clouds, obstacles, score):

    draw_screen(dino, ground, clouds, obstacles)
    death_text(score)
    draw_score(score)
    pygame.display.update()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
