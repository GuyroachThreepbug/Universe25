import pygame

def draw_game_screen(screen, font, day, colony, BeautifulOne):
    screen.fill((30, 30, 30))
    
    pygame.display.set_caption("Universe 25")

    text_surface = font.render(f"Colony size: {colony.size}", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topright = (800 - 10, 10)
    screen.blit(text_surface, text_rect)

    c = day.game_time()
    c_surface = font.render(f"{c}", True, (255, 255, 255))
    c_rect = c_surface.get_rect()
    c_rect.topleft = (50 - 10, 10)
    screen.blit(c_surface, c_rect)

    p = day.check_cal()
    p_surface = font.render(f"Day: {p}", True, (255, 255, 255))
    p_rect = p_surface.get_rect()
    p_rect.center = (400 - 10, 10)
    screen.blit(p_surface, p_rect) 
    
    f = BeautifulOne.frustration_points
    
    d = BeautifulOne.depression_points
    
        
    