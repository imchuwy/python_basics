'''
Testing different types of exceptions 
'''

divisionlist = [10,9,8,7,6,5,4,3,2,1,0]
x = input('divide by: ')

try:
    for number in divisionlist:
        print(number / int(x))
except ZeroDivisionError: #Exception for the division by 0 error
    print('Cannot divide by 0')
except ValueError:
    print('Caanot divide by non numerical')


