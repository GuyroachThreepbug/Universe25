import pygame
import mouseclasses
import functions

## frustration points might go down over time?
## dog?
class BeautifulOne():
    
    def __init__(self):
        self.frustration_points = 10
        self.max_frustration_points = 100
        self.depression_points = 20
        self.max_depression_points = 100
        ##self.schedule = schedule
        ##schedule will affect odds, trigger story events that may have status effects.
        ##depression is also supposed to affect the odds of being noticed
        
        
        
    def dice_roll(num_dice):
    
        roll = []
    
        for _ in range(num_dice):
            result = random.randint(1, 6)
            roll.append(result)
            score = sum(roll)
            return score
        
        
    def War(self):
        ##code for putting out traps
        ##render text narrating actions
        ##maybe another dice roll for how many?
        ##culling depends on average age of mice?
        modifier = []
        num_dice = random.randint(2, 5)
        outcome = dice_roll(num_dice)
        
        modifier += num_dice
        
        casualties = int(modifier)
        dead = dice_roll(modifier)
        
        Colony.size -= dead
        
        if dead < outcome:
            pass
        
        ##how to use number of traps left to affect death odds when foraging
        
    
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
            


