import pygame


class PauseManager:
    def __init__(self):
        self.total_paused = 0
        self.pause_started_at = None
        self.is_paused = False

    def pause(self):
        if not self.is_paused:
            self.is_paused = True
            self.pause_started_at = pygame.time.get_ticks()

    def unpause(self):
        if self.is_paused:
            self.is_paused = False
            paused_duration = pygame.time.get_ticks() - self.pause_started_at
            self.total_paused += paused_duration
            self.pause_started_at = None

    def get_adjusted_ticks(self):
        return pygame.time.get_ticks() - self.total_paused
    
