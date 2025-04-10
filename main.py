
import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    asteroidfield = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
        
    dt = 0
      
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        
        pygame.Surface.fill(screen,(0,0,0))

        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

    

if __name__ == "__main__":
    main()