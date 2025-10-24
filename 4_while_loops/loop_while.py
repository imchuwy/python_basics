# These condition keeps running until condition is met OR CTRL+D

number = 100
while number > 0:
    print(number)
    number //= 2


# This condition ask for user feedback until a "PW" is correct
password = ""
while password.lower() != "quit":
    password = input(">")
    print("ECHO", password)


# Careful about infinite loops. We can also remove the first password = ""
while True:
    command = input(">")
    print("ECHO", password)
    if command.lower() == "quit":
        break
