import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import sys


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x: float = SCREEN_WIDTH / 2
    y: float = SCREEN_HEIGHT / 2
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y)
    AsteroidField()
    
    dt: int = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                sys.exit('Game Over')

        screen.fill((0, 0, 0))
       
        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
