import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        else:
            random_angle = random.uniform(20, 50)
        
            rotate_cw = pygame.math.Vector2(self.velocity).rotate(random_angle)
            rotate_ccw = pygame.math.Vector2(self.velocity).rotate(-random_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = rotate_cw * 1.2
            
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = rotate_ccw * 1.2
        