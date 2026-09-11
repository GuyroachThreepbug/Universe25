#mainLoop

import pygame
from mouseclasses import *
import time
from BeautifulOne import *
import sys
from screen import *
import pygame_gui
from Pause import *
from PauseMenu import *

def main():    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    
    ##establish in-game time
    
    seconds_per_day = 24 * 60
    end = seconds_per_day * 1000


    manager = pygame_gui.UIManager((screen.get_width(), screen.get_height()))
    
    day = Day(max_turns=3, dur=end)
    
    running = True
    test = Colony(3, day)
    Beaut = BeautifulOne()
    home = nest(100, 100)
    
    
    faster = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),text='faster!', manager=manager)
    reset = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 350), (100, 50)),text='reset', manager=manager)
    FoodRun = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 425), (100, 50)),text='Forage', manager=manager)
    
    while running:
        real_delta_ms = clock.tick(60)
        time_delta = real_delta_ms / 1000.0
        day.advance(real_delta_ms)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not day.is_paused:
                        day.pause()
                        draw_pause_menu(screen, font)
                    else:
                        day.unpause()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == faster:
                    day.speed_up()
                    print("Speed Up button pressed!")
                if event.ui_element == reset:
                    day.reset_speed()
                    print("Reset button pressed!")
                if event.ui_element == FoodRun:
                    test.forage(Beaut)
            Colony.check_events(test, day)
            manager.process_events(event)
        manager.update(time_delta)


        draw_game_screen(screen, font, test, Beaut, home, day)        
        manager.draw_ui(screen)
        test.feed()
        pygame.display.flip()
        
    pygame.quit()


        

main()

