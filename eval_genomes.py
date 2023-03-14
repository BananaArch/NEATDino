import math
import os
import neat.nn
import pygame
import pickle
from pygame import mixer
from game.screen import *
from game.sfx import *
from actors.dinosaur import Dino
from actors.obstacles import Obstacles
from background.ground import Ground
from background.clouds import Clouds

TPS = 60
GEN = 0

# CHANGE GRAVITY ACC EFFECTS NN
# CHANGE OBSTACLE THRESHOLD THING EFFECTS NN

# inputs
#     dino y
#     obstacle_x1
#     obstacle_x2
#     obstacle_y1
#     obstacle_y2
#     dino_ducking
#     obstacle velocity
# outputs
#     jump [0,1]
#     duck [0,1]

def eval_genomes(genomes, config):

    global TPS
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    TPS *= 4
                if event.key == pygame.K_UP:
                    TPS *= 2
                if event.key == pygame.K_DOWN:
                    TPS /= 2
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    TPS /= 4


        if len(dinos) == 0:
            GEN += 1
            break

        #     NEURAL NET AND FITNESS

        for i, dino in enumerate(dinos):

            ge[i].fitness += 1
            # if dino.is_ducking:
            #     ge[i].fitness += 1

            dino.move()

            next_obstacle = obstacles.next_obstacle(dino)

            output = nets[i].activate((dino.y,
                                       next_obstacle.x,
                                       next_obstacle.x + next_obstacle.img.get_width(),
                                       next_obstacle.y,
                                       next_obstacle.y + next_obstacle.img.get_height(),
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

        if score > 99999:
            for g in ge:
                g.fitness += 100
            run = False

    play_gameover()
    print('Score {!s}'.format(round(score)))
    print('Velocity {!s}'.format(vel))

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_file)

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())

    winner = population.run(eval_genomes, 999)
    with open("winner", "wb") as f:
        pickle.dump(winner, f)
        f.close()
    print('\nBest genome:\n{!s}'.format(winner))
def replay_genome(config_file, genome_path="1.3g, (.2, .4).pkl"):

    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_file)

    with open(genome_path, "rb") as f:
        genome = pickle.load(f)

    genomes = [(1, genome)]
    eval_genomes(genomes, config)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    # run(config_path)
    replay_genome(config_path)