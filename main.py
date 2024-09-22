import pygame
from player import Player
from constants import *


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
    Player.containers = (updatable, drawable)
   
    player = Player(x, y)
    
    dt: int = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)
        

        pygame.display.flip()
        


if __name__ == "__main__":
    main()
