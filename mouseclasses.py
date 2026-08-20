
import time
import pygame
import random
##replacing last_brood with pygame event trigger


class Colony():
    
    def __init__(self, size, pause_manager):
        self.size = size
        self.nest = None
        self.hunger = None
        self.babies = 0
        self.pause_manager = pause_manager
        self.breed_interval = 1260000
        self.grow_interval = 2520000
        self.last_breed = pause_manager.get_adjusted_ticks()
        self.last_grow = pause_manager.get_adjusted_ticks()
    
    def reproduce(self):
        pair = int(self.size / 2)
        make = pair * 3
        self.babies += make
        print(f"babies: {self.babies}")

    def moveUp(self):
        self.size += self.babies
        self.babies = 0
        print(f"size: {self.size}")

    def check_events(self):
        now = self.pause_manager.get_adjusted_ticks()
        
        if now - self.last_breed >= self.breed_interval:
            self.reproduce()
            self.last_breed = now
        if now - self.last_grow >= self.grow_interval:
            self.moveUp()
            self.last_grow = now 

class hunger_meter():
    def __init__(self, size):
        self.size = size
            
class nest():
    
    def __init__(self, location, capasity, storage):
        self.Colony = Colony
        self.location = location
        self.storage = storage
        self.capasity = capasity
        pass
    
    def GreatEscape(self):
        if Colony >= self.capasity:
            escapees = random.randint(1, 6)
            Colony -= escapees
            return Colony.size

class mouse():
    
    def __init__(self, sex, age):
        self.sex = sex
        self.age = age
        