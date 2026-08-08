
import time
import pygame
import random
##replacing last_brood with pygame event trigger


class Colony():
    
    def __init__(self, size):
        self.size = size
        self.nest = None
        self.hunger = None
        self.babies = 0
    
    def reproduce(self):
        pair = int(self.size / 2)
        make = pair * 3
        self.babies += make
        print(self.babies)

    def moveUp(self):
        self.size += self.babies
        self.babies = 0
        print(self.size)

    def hunger_meter():
    
class nest():
    
    def __init__(self, location, capasity, storage):
        self.Colony = Colony
        self.location = location
        self.storage = storage
        self.capasity = capasity

    def GreatEscape():
        if Colony >= self.capasity:
            escapees = random.randint(1, 6)
            Colony -= escapees
            return Colony.size

class mouse():
    
    def __init__(self, sex, age):
        self.sex = sex
        self.age = age
        