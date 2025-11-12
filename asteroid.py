from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event('asteroid_split')
        ran = random.uniform(20,50)

        newVector1 = self.velocity.rotate(ran)
        newVector2 = self.velocity.rotate(-ran)
        
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        newAst1 = Asteroid(self.position.x, self.position.y, newRadius)
        newAst2 = Asteroid(self.position.x, self.position.y, newRadius)

        newAst1.velocity = newVector1 * 1.2
        newAst2.velocity = newVector2 * 1.2
