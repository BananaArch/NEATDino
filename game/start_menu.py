from game.screen import *
from game.sfx import *

def start_menu(dino, ground, clouds, obstacles):

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    run = False
                    dino.is_jumping = True
                if event.key == pygame.K_RETURN:
                    run = False

        draw_screen(dino, ground, clouds, obstacles, score=0)
        start_screen()
        pygame.display.update()

    play_player_action()