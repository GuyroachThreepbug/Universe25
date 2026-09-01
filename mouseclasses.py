
import time
from Gametime import *
import pygame
import random
##replacing last_brood with pygame event trigger


class Colony():
    
    def __init__(self, size, pause_manager, day):
        self.size = size
        self.nest = nest
        self.hunger = 2
        self.babies = 0
        self.pause_manager = pause_manager
        self.breed_interval = random.randint(1260000, 1440000)
        self.grow_interval = 2520000
        self.last_breed = pause_manager.get_adjusted_ticks()
        self.last_grow = pause_manager.get_adjusted_ticks()
        self.food_demand = self.size * 3
        self.stockpile = 0
        self.feed_rate = self.food_demand / day.dur
        
    def reproduce(self):
        pair = int(self.size / 2)
        make = pair * random.randint(1, 5)
        self.babies += make
        print(f"babies: {self.babies}")

    def moveUp(self):
        self.size += self.babies
        self.babies = 0
        print(f"size: {self.size}")

    def check_events(self):
        now = self.pause_manager.get_adjusted_ticks()
        
        self.feed()
        
        if now - self.last_breed >= self.breed_interval:
            self.reproduce()
            self.last_breed = now
        if now - self.last_grow >= self.grow_interval:
            self.moveUp()
            self.last_grow = now
        
    
    def feed(self):
        
        if self.stockpile > 0:
            if self.hunger >= 0:  
                self.stockpile -= self.feed_rate
                self.hunger += self.feed_rate
        else:
            self.hunger -= self.feed_rate
        
        return self.stockpile, self.hunger
class nest():
    
    def __init__(self, capasity, storage):
        self.Colony = Colony
        self.location = self.location
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
        