import pygame
import os

pygame.display.init()
pygame.font.init()

LARGE_FONT = pygame.font.Font(os.path.join('assets', 'eight-bit_madness.ttf'), 72)
MEDIUM_FONT = pygame.font.Font(os.path.join('assets', 'eight-bit_madness.ttf'), 48)
SMALL_FONT = pygame.font.Font(os.path.join('assets', 'eight-bit_madness.ttf'), 32)

# original font is https://fonts.google.com/specimen/Press+Start+2P but I think 8bit looks nicer

DINO_SPRITE_SHEET_IMG = pygame.image.load(os.path.join('assets', 'dino_sprite_sheet.png'))
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DINO GAME')

def get_image(**kwargs):
    image = pygame.Surface((kwargs['w'], kwargs['h']), pygame.SRCALPHA, 32)
    image.blit(DINO_SPRITE_SHEET_IMG, (0, 0), (kwargs['x'], kwargs['y'], kwargs['w'], kwargs['h']))
    image = image.convert_alpha()
    return image

def start_screen():
    start_text = MEDIUM_FONT.render('Press space to play', False, GRAY, None)
    screen.blit(start_text, (20, 20))
def draw_screen(dino, ground, clouds, obstacles, score):

    screen.fill(WHITE)
    ground.draw(screen)
    clouds.draw(screen)
    dino.draw(screen)
    obstacles.draw(screen)
    text = MEDIUM_FONT.render("{:05d}".format(round(score)), False, GRAY, None)
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 20, 20))

def draw_neat_screen(dinos, ground, clouds, obstacles, score, generation, dinos_alive):

    screen.fill(WHITE)
    ground.draw(screen)
    clouds.draw(screen)
    for dino in dinos:
        dino.draw_alpha(screen)

    obstacles.draw(screen)

    score_text = MEDIUM_FONT.render("{:05d}".format(round(score)), False, GRAY, None)
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 20, 20))

    dinos_alive_text = SMALL_FONT.render("Alive {:02d}".format(dinos_alive), False, GRAY, None)
    dinos_alive_pos = (SCREEN_WIDTH - dinos_alive_text.get_width() - 20, score_text.get_height() + dinos_alive_text.get_height() + 10)
    screen.blit(dinos_alive_text, dinos_alive_pos)

    gen_text = SMALL_FONT.render("Gen {:02d}".format(generation), False, GRAY, None)
    gen_pos = (SCREEN_WIDTH - gen_text.get_width() - 20, score_text.get_height() + dinos_alive_text.get_height() + gen_text.get_height() + 10)
    screen.blit(gen_text, gen_pos)

def death_text():
    text = LARGE_FONT.render("GAME OVER", False, GRAY, None)
    screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, (.4 * SCREEN_HEIGHT - text.get_height()) // 2))

def replay_button(button_img, button_rect):
    screen.blit(button_img, button_rect)