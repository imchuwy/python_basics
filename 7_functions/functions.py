# Functions. Allow reusablility of our code
def greet():
    print("Hi there")
    print("Welcome aboard")

# greet()


# Arguments. Allows inputs
def hello(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

# hello("Oscar", "Chu")


# Example 3
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Oscar")
# print(message)


# Example 4.
# Use =1 to set default optional parameter
def increment(number, by=1, this=2):
    return number + by + this


# Use =1 in the input to show what argument is for
# print(increment(2, 1, 3))
# print(increment(number=2, by=2, this=2))

# Example 5. ARGs. Variable number of arguments. Use *

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# [] Tuples
# () List
