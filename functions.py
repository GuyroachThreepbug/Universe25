import random
import BeautifulOne


def dice_roll(num_dice):
    
    roll = []
    
    for _ in range(num_dice):
        result = random.randint(1, 6)
        roll.append(result)
        score = sum(roll)
    return score

def forage():
    score = dice_roll(2)
    if score >= 8:
        food_storage += 5
        hunger -= 5
    elif score >= 5 and score <= 7:
        hunger -= 3
    else:
        frustration_points += 5
        
def improve_nest():
    
    ##improving nest lessens the chance of young mice leaving the nest and getting caught/killed
    
    score = dice_roll()
    pass

