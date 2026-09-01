import pygame

def draw_game_screen(screen, font, day, colony, BeautifulOne):
    screen.fill((30, 30, 30))
    
    pygame.display.set_caption("Universe 25")


##colony count display
    text_surface = font.render(f"Colony size: {colony.size}", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topright = (800 - 10, 10)
    screen.blit(text_surface, text_rect)

##in-game time display

    c = day.game_time()
    c_surface = font.render(f"{c}", True, (255, 255, 255))
    c_rect = c_surface.get_rect()
    c_rect.topleft = (50 - 10, 10)
    screen.blit(c_surface, c_rect)


##days passed display
    p = day.check_cal() + 1
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
    pygame.draw.rect(screen, (0, 255, 0), fill_rect)
    
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
    pygame.draw.rect(screen, (0, 0, 255), fill_rect)
    
## hunger display

    h = colony.hunger
    demand = colony.food_demand
    
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
    pygame.draw.rect(screen, (255, 0, 0), fill_rect)   
    
    ## remaining turns display
    
    ## food storage display
    
    ## dice roll display
    
    ## flavortext display 