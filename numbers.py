# floats, ints, decimals, complex numbers (j)
# addition +
# Subtraction -
# Multiplication *
# Division (float) /
# Divions (int) //
# Modulus %
# Exponent **


# Augmented assignment operator (x = x + 3) same as (x += 3)


# functions e.g. round, abs,
round_number = round(2.9)
# print(round_number)

# math module has many functions @import math

# The input function will prompt the user to enter an input
x = input("x: ")
# The above input is currently as string. String cannot be added to int. Therefore below must be cast to int
y = int(x) + 1
z = (f"x: {x}. y: {y}")


# booleans Falsy =  ("", 0, None). ALL strings are true
b = bool("")


print(z)
