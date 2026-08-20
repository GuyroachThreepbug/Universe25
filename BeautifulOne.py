import pygame
import mouseclasses
import functions

## frustration points might go down over time?

class BeautifulOne():
    
    def __init__(self, frustration_points, depression_points):
        self.frustration_points = 0
        self.depression_points = 0

    def frustration_meter(frustration_points):
        pass
    
    def depression_meter(depression_points):
        pass
        
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
            


