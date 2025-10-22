'''
3h42

Write program to roll 2 dice
Class: Dice
    Method: Roll
        Returns tuple of two numbers (x, y)

'''
import random

class Dice:
    def roll(self):
        output = ()
        x = random.randint(1,6)
        y = random.randint(1,6)
        return x, y #This is automatically interpreted as a tuple


print(Dice().roll())