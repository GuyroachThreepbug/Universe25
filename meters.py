import pygame
import mouseclasses
import functions

## might be better to create a Beautiful One class with methods to handle frustration and depression
class BeautifulOne():
    
    def __init__(self, frustration_points, depression_points):
        self.frustration_points = frustration_points
        self.depression_points = depression_points

    def frustration_meter(frustration_points):
        pass
    
    def depression_meter(depression_points):
        pass
        
    def War():
        ##code for putting out traps
        ##maybe another dice roll for how many?
        ##culling depends on average age of mice?
        pass
    
    def trying():
        ##code reducing food availability
        ##cleanup
        pass
    
    def wtf():
        ##poison dropped behind the couch, stove
        ##depression meter goes up
        pass
    
    def triggerd():
        if self.frustration_points >= 50:
            War()
        if self.frustration_points >= 20 and self.frustration_points <= 49:
            trying()
        if self.frustration_points >= 10 and self.frustration_points <= 19:
            wtf()
        pass
            
            
class depression_meter():
    def __init__(depression_points):
        
        ##depression points debuff frustration, or add dice to dice pool since bo is less likely to notice
        
        pass



class day():
    def __init__(self, turns, dur, past):
        self.turns = turns
        self.dur = dur
        self.past = past
        pass