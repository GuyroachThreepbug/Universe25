
import pygame


class Day():
    def __init__(self, max_turns, dur, pause_manager):
        self.max_turns = max_turns
        self.turns_remaining = 3
        self.dur = dur
        self.past = 0
        self.pool = 2
        self.pause_manager = pause_manager
        pass
    
    def check_cal(self):
        total = self.pause_manager.get_adjusted_ticks()
        self.past = total // self.dur
        print(self.past)
        return self.past
    
    def game_time(self):
        total = self.pause_manager.get_adjusted_ticks()
        today = total % self.dur
        seconds = today // 1000
        h = seconds // 60
        m = seconds % 60           
        return f"{h:02d}:{m:02d}"
    
    def morning(self):
        pass
    
    def evening(self):
        pass
    
    def night(self):
        pass