import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatables)
    asteroidfield = AsteroidField()
    Asteroid.containers = (asteroids, updatables, drawables)

    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        screen.fill(color=0x000000)

        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collided(shot):
                    asteroid.kill()
                    shot.kill()

            if asteroid.collided(player):
                print("Game over!")
                return

        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
    
