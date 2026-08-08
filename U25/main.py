#mainLoop
import pygame
from mouseclasses import *
import time
from meters import *


def main():    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    
    BREED = pygame.USEREVENT
    GROW = pygame.USEREVENT  + 1 
    pygame.time.set_timer(BREED,1260000)
    pygame.time.set_timer(GROW, 2520000)
    
    running = True
    
    test = Colony(3)
    
    while running:
        for event in pygame.event.get():
            if event.type == BREED:
                Colony.reproduce(test)
            if event.type == GROW:
                Colony.moveUp(test)
    
            screen.fill((30, 30, 30))
    
            text_surface = font.render(f"Colony size: {test.size}", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.topright = (800 - 10, 10)
            screen.blit(text_surface, text_rect)            
    
            pygame.display.flip()
            clock.tick(60)
    pygame.quit()


        

main()

