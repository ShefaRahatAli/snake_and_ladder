import random 

class Dice:
    MIN = 1

    def __init__(self, number_of_dice):
        self.number_of_dice = number_of_dice

    def roll(self):
        return random.randint(Dice.MIN, self.number_of_dice)