import pygame
import mouseclasses
import functions

## frustration points might go down over time?

class BeautifulOne():
    
    def __init__(self):
        self.frustration_points = 10
        self.max_frustration_points = 100
        self.depression_points = 20
        self.max_depression_points = 100
        
    def War(self):
        ##code for putting out traps
        ##render text narrating actions
        ##maybe another dice roll for how many?
        ##culling depends on average age of mice?
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
            


