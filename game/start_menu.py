from game.screen import *


def start_menu(dino, ground, clouds, obstacles):
    draw_screen(dino, ground, clouds, obstacles)

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

        start_screen()
        draw_score(0)
        pygame.display.update()