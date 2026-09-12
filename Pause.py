import pygame

class Day:
    def __init__(self, max_turns, dur):
        self.max_turns = max_turns
        self.turns_remaining = 3
        self.dur = dur
        self.past = 0
        self.yesterday = 0
        self.pool = 2

        self.is_paused = False
        self.world_speed = 1.0
        self.elapsed = 0   # renamed from game_time to avoid clashing with the method below

    def advance(self, real_delta_ms):
        if not self.is_paused:
            self.elapsed += real_delta_ms * self.world_speed

    def get_adjusted_ticks(self):
        return self.elapsed

    def pause(self):
        self.is_paused = True

    def unpause(self):
        self.is_paused = False

    def speed_up(self):
        self.world_speed *= 2.0
        print(f"World speed increased to {self.world_speed}x")

    def reset_speed(self):
        self.world_speed = 1.0
        print("World speed reset to normal")

    def check_cal(self):
        total = self.get_adjusted_ticks()
        self.past = int(total // self.dur)
        return self.past

    def game_time(self):
        total = self.get_adjusted_ticks()
        today = total % self.dur
        seconds = int(today // 1000)
        h = seconds // 60
        m = seconds % 60
        return f"{h:02d}:{m:02d}"
    
    def new_day(self):
        current = self.check_cal()
        if current != self.yesterday:
            self.yesterday = current
            return True
        return False
    
    def turn_manager(self):
        if self.new_day():
            self.turns_remaining = self.max_turns