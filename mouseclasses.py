
import time


import pygame
import random
##replacing last_brood with pygame event trigger


class Colony():
    
    def __init__(self, size, day):
        self.size = size
        self.nest = nest
        self.hunger = 2
        self.babies = 0
        self.breed_interval = random.randint(1260000, 1440000)
        self.grow_interval = 2520000
        self.last_breed = day.get_adjusted_ticks()
        self.last_grow = day.get_adjusted_ticks()
        self.food_demand = self.size * 3
        self.stockpile = 5
        self.feed_rate = self.food_demand / (day.dur / 500)
        self.dice_pool = 3

    def reproduce(self):
        pair = int(self.size / 2)
        make = pair * random.randint(1, 5)
        self.babies += make
        print(f"babies: {self.babies}")

    def moveUp(self):
        self.size += self.babies
        self.babies = 0
        print(f"size: {self.size}")

    def check_events(self, day):
        now = day.get_adjusted_ticks()
        
        if now - self.last_breed >= self.breed_interval:
            self.reproduce()
            self.last_breed = now
        if now - self.last_grow >= self.grow_interval:
            self.moveUp()
            self.last_grow = now
        
    
    def feed(self,day):
        if not day.is_paused:
            if self.stockpile > 0:
                if self.hunger >= 0:  
                    self.stockpile -= self.feed_rate
                    self.hunger += self.feed_rate
                    print("chompchomp")
                    print(f"Stockpile: {self.stockpile}, Hunger: {self.hunger}")
            else:
                self.hunger -= self.feed_rate
                print("chomp")
    
    def dice_roll(self, dice_pool):
    
        roll = []
    
        for _ in range(dice_pool):
            result = random.randint(1, 6)
            roll.append(result)
            score = sum(roll)
            return score
    
    def forage(self, Beaut):
        score = self.dice_roll(self.dice_pool)
        if score >= 8:
            self.stockpile += 5
            self.hunger -= 5
        elif score >= 5 and score <= 7:
            self.hunger -= 3
        else:
            Beaut.frustration_points += 5
            
    def fresh_out(self):
        if self.hunger == 0:
            self.size -= 1
        pass
            
            
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
        