
import time
from Gametime import *
import pygame
import random
##replacing last_brood with pygame event trigger


class Colony():
    
    def __init__(self, size, pause_manager, Day):
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
        self.stockpile = 5
        self.feed_rate = self.food_demand / Day.dur
        
    def reproduce(self):
        pair = int(self.size / 2)
        make = pair * random.randint(1, 5)
        self.babies += make
        return self.babies

    def moveUp(self):
        self.size += self.babies
        self.babies = 0
        return self.size

    def check_events(self):
        now = self.pause_manager.get_adjusted_ticks()
                
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
                print("chomp")
        else:
            self.hunger -= self.feed_rate
    
    def dice_roll(num_dice):
    
        roll = []
    
        for _ in range(num_dice):
            result = random.randint(1, 6)
            roll.append(result)
            score = sum(roll)
            return score
    
    def forage(self):
        if self.stockpile >= nest.storage:
            ##come back later to implement mechanic
            return
        else:
            haul = diceroll(3)
            if haul >= 10:
                self.stockpile += 6
                ##rotating flavor text about what items were found - success roll
            if haul >= 6:
                self.stockpile += 3
                ##flavor text explaining why haul is low
            else:
                BeautifulOne.frustration_points += 2
    
            
class nest():
    
    def __init__(self, capasity, storage):
        self.Colony = Colony
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
        