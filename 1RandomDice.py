# https://www.youtube.com/watch?v=yVl_G-F7m8c
# 1. Roll a random dice
import numpy as np

# loop
while True:
    # Ask user to roll dice
    check = input("Roll the dice (y/n): ")
# If user enter y
    if check.lower() == "y":
        # Then generate random numbers
        print(np.random.randint(1, 7))
    elif check.lower() == "n":
        print('Thank you')
        break
    else:
        print('Error')
