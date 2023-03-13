import math
import os
import neat.nn
import pygame
from pygame import mixer
from game.screen import *
from game.sfx import *
from actors.dinosaur import Dino
from actors.obstacles import Obstacles
from background.ground import Ground
from background.clouds import Clouds

TPS = 60 * 2
GEN = 0


# inputs
#     dino y
#     obstacle_x1
#     obstacle_x2
#     obstacle_y1
#     obstacle_y2
#     obstacle velocity
# outputs
#     jump [0,1]
#     duck [0,1]

def eval_genomes(genomes, config):

    global GEN
    ground = Ground()
    clouds = Clouds()
    obstacles = Obstacles()
    vel = 10
    score = 0
    clock = pygame.time.Clock()

    nets = []
    ge = []
    dinos = []

    for _, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        dinos.append(Dino(100))
        genome.fitness = 0
        ge.append(genome)

    run = True
    while run:

        clock.tick(TPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if len(dinos) == 0:
            GEN += 1
            run = False

        #     NEURAL NET AND FITNESS

        for i, dino in enumerate(dinos):

            ge[i].fitness += .1
            # if dino.is_ducking:
            #     ge[i].fitness += .1

            dino.move()

            next_obstacle = obstacles.next_obstacle(dino)

            output = nets[i].activate((dino.y,
                                       next_obstacle.x,
                                       next_obstacle.x + next_obstacle.img.get_width(),
                                       next_obstacle.y,
                                       next_obstacle.y + next_obstacle.img.get_height(),
                                       dino.is_ducking,
                                       vel))

            dino.is_jumping = output[0] > 0
            dino.is_ducking = output[1] > 0 and not dino.is_jumping

            if obstacles.has_collided(dino):
                dinos.pop(i)
                nets.pop(i)
                ge.pop(i)


        obstacles.move(vel)
        ground.move(vel)
        clouds.move(vel / 10)

        draw_neat_screen(dinos, ground, clouds, obstacles, score, GEN, len(dinos))
        pygame.display.update()

        obstacles.update_obstacles()

        score += .05 + score / 2000

        vel = vel + .002 if vel < 25 else 25

        # goes 100, 200, 300 ... , 1000, 2000, 3000 ...
        if round(score) % math.pow(10, math.floor(math.log10(score))) == 0 and score >= 100:
            play_achievement()

    play_gameover()
    print('Score {!s}'.format(round(score)))

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_file)

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())

    winner = population.run(eval_genomes, 100)
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)