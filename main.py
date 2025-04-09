
import pygame
from player import Player

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        
        pygame.Surface.fill(screen,(0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

    

if __name__ == "__main__":
    main()