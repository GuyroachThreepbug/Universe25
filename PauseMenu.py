
import pygame

def draw_pause_menu(screen, font):
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Universe 25 -- paused")
    text_surface = font.render("Paused - Press Pause to Resume", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)