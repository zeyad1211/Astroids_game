from constants import *
import pygame
from player import Player
def main():
    pygame.init()
    clk = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()    
    Player.containers = (updatable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shooter = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        
        dt = clk.tick(60)/1000
        for obj in drawable:
           obj.draw(screen)
           
        updatable.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
