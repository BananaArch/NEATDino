from screen import *
from dinosaur import Dino
from obstacles.obstacles import Obstacles
from background.ground import Ground
from background.clouds import Clouds
from game.start_menu import start_menu

TPS = 60

# stuff to implement

# NEAT
# death screen
def main():
    dino = Dino(100)
    ground = Ground()
    clouds = Clouds()
    obstacles = Obstacles()
    vel = 10
    score = 0

    start_menu(dino, ground, clouds, obstacles)

    clock = pygame.time.Clock()

    run = True
    while run:

        dt = clock.tick(TPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.is_jumping = True
                if event.key == pygame.K_DOWN:
                   dino.is_ducking = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    dino.is_jumping = False
                if event.key == pygame.K_DOWN:
                    dino.is_ducking = False


        obstacles.update_obstacles()

        dino.move()
        obstacles.move(vel * dt * TPS / 1000)
        ground.move(vel * dt * TPS / 1000)
        clouds.move((vel * dt * TPS / 1000) / 10)

        draw_screen(dino, ground, clouds, obstacles)
        draw_score(score)
        pygame.display.update()


        if obstacles.has_collided(dino):
            main()

        score += .025 + score / 1250
        vel = vel + .0015 if vel < 20 else 20



main()
