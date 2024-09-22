import pygame
from constants import *
from asteroid import Asteroid
from circleshape import CircleShape


class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1)
        

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)


    