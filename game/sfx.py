import pygame
import os

pygame.mixer.init()
pygame.mixer.set_num_channels(3)

PLAYER_ACTION = pygame.mixer.Sound(os.path.join('assets', 'player-action.mp3'))
GAMEOVER = pygame.mixer.Sound(os.path.join('assets', 'gameover.mp3'))
ACHIEVEMENT = pygame.mixer.Sound(os.path.join('assets', 'achievement.mp3'))

def play_player_action():
    pygame.mixer.Channel(0).play(PLAYER_ACTION)
def play_achievement():
    pygame.mixer.Channel(1).play(ACHIEVEMENT)

def play_gameover():
    pygame.mixer.Channel(2).play(GAMEOVER)