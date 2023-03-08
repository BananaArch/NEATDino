import pygame
import os

pygame.display.init()
pygame.font.init()

# largeText = pygame.font.Font('freesansbold.ttf',90)

DINO_SPRITE_SHEET_IMG = pygame.image.load(os.path.join('assets', 'dino_sprite_sheet.png'))
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BG = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DINO GAME')

def get_image(**kwargs):
    image = pygame.Surface((kwargs['w'], kwargs['h']), pygame.SRCALPHA, 32)
    image = image.convert_alpha()
    image.blit(DINO_SPRITE_SHEET_IMG, (0, 0), (kwargs['x'], kwargs['y'], kwargs['w'], kwargs['h']))
    return image

def start_screen():
    pass

def draw_screen(dino, ground, cloud, obstacles):
    screen.fill(BG)

    ground.draw(screen)
    cloud.draw(screen)
    dino.draw(screen)
    obstacles.draw(screen)

    pygame.display.update()

def death_text():
    # text = largeText.render("GAME OVER")
    pass