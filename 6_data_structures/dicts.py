'''Dictionaries
Dicts are for key value pairs
{} Defines Dicts
'''
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
#customer["birthdate"] = "2025-01-01" #We can add value pairs into the dict
#print(customer["name"]) #Can select specific key
#print(customer.get("gender", "M")) #Can select and create default
#print(customer)


#Challenge
#Input numbers e.g. phone = 1234. Print the varchar
map = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
phone = input("Phone: ")
for ch in phone:
    map.get(ch, "!")
    output += map.get(ch, "!") + " "
print(output)
