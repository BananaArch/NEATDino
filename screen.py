import pygame
import os

pygame.display.init()
pygame.font.init()

LARGE_FONT = pygame.font.Font(os.path.join('assets', 'Eight-Bit Madness.ttf'), 64)
MEDIUM_FONT = pygame.font.Font(os.path.join('assets', 'Eight-Bit Madness.ttf'), 48)


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
def draw_screen(dino, ground, clouds, obstacles):

    screen.fill(WHITE)
    ground.draw(screen)
    clouds.draw(screen)
    dino.draw(screen)
    obstacles.draw(screen)

def draw_score(score):
    text = MEDIUM_FONT.render("{:05d}".format(round(score)), False, GRAY, None)
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 20, 20))

def death_text(score):
    text = LARGE_FONT.render("GAME OVER", False, GRAY, None)
    screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, (.4 * SCREEN_HEIGHT - text.get_height()) // 2))

def replay_button(button_img, button_rect):
    screen.blit(button_img, button_rect)