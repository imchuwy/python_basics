'''
In this exercise. We have the below code from earlier.
This is code which loops over list to return the largest number.
We want to make this a module which we call in pr_mod_utils.py

list = [10,2,6,11,5]
max = list[0] # Takes 1st item in list
for number in list:
    if number > max:
        max = number
print(max)

'''

def find_max(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return max