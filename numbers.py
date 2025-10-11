# floats, ints, decimals, complex numbers (j)
# addition +, subtraction -, multiplication *, division (float) /, (int) //
# modulus %, exponent **
# augmented assignment operator: (x = x + 3) same as (x += 3)
# functions e.g. round(), abs()

round_number = round(2.9)
# print(round_number)

# math module has many functions — import using: import math

# The input function will prompt the user to enter an input
x = input("x: ")

# The above input is a string. To use it as a number, cast to int
y = int(x) + 1
z = f"x: {x}, y: {y}"

# Booleans: Falsy values = ("", 0, None). All non-empty strings are True
b = bool("")

print(z)
print(f"Boolean value of empty string: {b}")
