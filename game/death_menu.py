import pygame
from screen import *
from sprites import *

REPLAY_IMG = REPLAY_ICON_IMG
BUTTON_POSITION = ((SCREEN_WIDTH - REPLAY_IMG.get_width()) // 2, (SCREEN_HEIGHT - REPLAY_IMG.get_height()) // 2)

def death_menu(dino, ground, clouds, obstacles, score):

    button_img = REPLAY_IMG
    button_rect = button_img.get_rect(topleft=BUTTON_POSITION)


    draw_screen(dino, ground, clouds, obstacles)
    death_text(score)
    replay_button(button_img, button_rect)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        run = False

