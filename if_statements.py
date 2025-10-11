temp = 21

# Don't forget the : at the end of the IF. Indentations matter!
if temp > 30:
    message = "It's hot"
elif temp > 20:
    message = "It's warm"
else:
    message = "It's cold"
# Last statemnt has indentation removed to show end of block
# print(message)

# Ternary operator. Does not use elif
age = 13
gender = 'F'
output = (
    "Adult Male" if (age >= 18 and gender == 'M')
    else "Adult Female" if (age >= 18 and not gender == 'M')
    else "Teen" if 18 > age >= 12
    else "Not adult"
)
print(output)
