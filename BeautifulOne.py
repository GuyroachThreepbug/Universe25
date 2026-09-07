import random

import pygame
import mouseclasses
import functions

## frustration points might go down over time?

class BeautifulOne():
    
    def __init__(self):
        self.frustration_points = 10
        self.max_frustration_points = 100
        self.depression_points = 100
        self.max_depression_points = 100
        
    def War(self):
        ##code for putting out traps
        ##render text narrating actions
        ##maybe another dice roll for how many?
        ##culling depends on average age of mice?
        num_dice = random.randint(1, 5)
        dice_roll = functions.dice_roll(num_dice)
        
        ##one dice roll to determine number of traps, another to determine how many mice are caught
        ##if num killed less than num traps, chance to get caught in traps during action turns 
        
        pass
    
    def trying(self):
        ##code reducing food availability
        ##cleanup
        pass
    
    def wtf(self):
        ##poison dropped behind the couch, stove
        ##depression meter goes up
        pass
    
    def triggerd(self):
        if self.frustration_points >= 50:
            self.War()
        if self.frustration_points >= 20 and self.frustration_points <= 49:
            self.trying()
        if self.frustration_points >= 10 and self.frustration_points <= 19:
            self.wtf()
        return
            


