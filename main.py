
import pygame

from constants import (SCREEN_HEIGHT,
                       SCREEN_WIDTH,
                       ASTEROID_KINDS,
                       ASTEROID_MAX_RADIUS,
                       ASTEROID_MIN_RADIUS,
                       ASTEROID_SPAWN_RATE)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()

    

if __name__ == "__main__":
    main()