#mainLoop
import pygame
from mouseclasses import *
import time
from BeautifulOne import *
import sys
from Gametime import *
from Pause import *
from PauseMenu import *
from screen import *


def main():    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    
    ##establish in-game time
    
    seconds_per_day = 24 * 60
    end = seconds_per_day * 1000


    pause_manager = PauseManager()  
    day = Day(max_turns=3, dur=end, pause_manager=pause_manager)
    
    running = True
    
    test = Colony(3, pause_manager)
    TBO = BeautifulOne()
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pause_manager.is_paused:
                        pause_manager.unpause()
                    else:
                        pause_manager.pause()
        if pause_manager.is_paused:
            draw_pause_menu(screen, font)
        else:
            test.check_events()
            draw_game_screen(screen, font, day, test, TBO)

        pygame.display.flip()
            
        clock.tick(60)
        
    pygame.quit()


        

main()

