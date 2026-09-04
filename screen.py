import pygame
import pygame_widgets
from pygame_widgets.button import ButtonArray

def draw_game_screen(screen, font, Day, Colony, BeautifulOne, nest):
    screen.fill((30, 30, 30))
    
    pygame.display.set_caption("Universe 25")


##colony count display
    text_surface = font.render(f"Colony size: {Colony.size}", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topright = (800 - 10, 10)
    screen.blit(text_surface, text_rect)

##in-game time display

    c = Day.game_time()
    c_surface = font.render(f"{c}", True, (255, 255, 255))
    c_rect = c_surface.get_rect()
    c_rect.topleft = (50 - 10, 10)
    screen.blit(c_surface, c_rect)


##days passed display
    p = Day.check_cal() + 1
    p_surface = font.render(f"Day: {p}", True, (255, 255, 255))
    p_rect = p_surface.get_rect()
    p_rect.center = (400 - 10, 10)
    screen.blit(p_surface, p_rect) 
        
###frustration meter display
    
    f = BeautifulOne.frustration_points
    fm = BeautifulOne.max_frustration_points
    x, y, width, height = 50, 50, 25, 300
    
    fm_rect = pygame.Rect(x, y, width, height)
    fm_rect.bottomleft = (50, 590)
    pygame.draw.rect(screen, (60, 60, 60), fm_rect)
    pygame.draw.rect(screen, (255, 255, 255), fm_rect, 2)

    ratio = f / fm
    fill_height = int(height * ratio)
    
    # 3. Fill rect position shifts down as height shrinks
    fill_y = y + (height - fill_height)
    fill_rect = pygame.Rect(x, fill_y, width, fill_height)
    fill_rect.bottomleft = (50, 590)
    pygame.draw.rect(screen, (74, 4, 4), fill_rect)
    
## depression meter display
    
    d = BeautifulOne.depression_points
    dm = BeautifulOne.max_depression_points
    
    x, y, width, height = 10, 10, 25, 300
    
    dm_rect = pygame.Rect(x, y, width, height)
    dm_rect.bottomleft = (10, 590)
    pygame.draw.rect(screen, (60, 60, 60), dm_rect)
    pygame.draw.rect(screen, (255, 255, 255), dm_rect, 2)

    ratio = d / dm
    fill_height = int(height * ratio)

    # 3. Fill rect position shifts down as height shrinks
    fill_y = y + (height - fill_height)
    fill_rect = pygame.Rect(x, fill_y, width, fill_height)
    fill_rect.bottomleft = (10, 590)
    pygame.draw.rect(screen, (137, 207, 240), fill_rect)
    
## hunger display

    h = Colony.hunger
    demand = Colony.food_demand
    
    x, y, width, height = 750, 10, 25, 300
    
    demand_rect = pygame.Rect(x, y, width, height)
    demand_rect.bottomleft = (750, 590)
    pygame.draw.rect(screen, (60, 60, 60), demand_rect)
    pygame.draw.rect(screen, (255, 255, 255), demand_rect, 2)
    
    ratio = h / demand
    fill_height = int(height * ratio)
    
    fill_y = y + (height - fill_height)
    fill_rect = pygame.Rect(x, fill_y, width, fill_height)
    fill_rect.bottomleft = (750, 590)
    pygame.draw.rect(screen, (53, 94, 59), fill_rect)   
    
    ## remaining turns display
    
    ## food storage display
    s = nest.storage
    p = Colony.stockpile
    
    x, y, width, height = 710, 10, 25, 300
    stockpile_rect = pygame.Rect(x, y, width, height)
    stockpile_rect.bottomleft = 710, 590
    pygame.draw.rect(screen, (60, 60, 60), stockpile_rect)
    pygame.draw.rect(screen, (255, 255, 255), stockpile_rect, 2)
    
    ratio = p / s
    fill_height = int(height * ratio)
    
    fill_y = y + (height - fill_height)
    fill_rect = pygame.Rect(x, fill_y, width, fill_height)
    fill_rect.bottomleft = (710, 590)
    pygame.draw.rect(screen, (156, 175, 136), fill_rect)
    ## dice roll display
    
    ## flavortext display
    
    ## action buttons moved to main