'''
2h54m
exit code 0 = Success
exit code 1 (anything else) = Crash

We don't want crashes due to incorrect value. Better print an error message

This below is called 'error handling'
'''
try:
    age = int(input('Age: '))
    income = 30000
    risk = income / age
    print(age)
except ValueError: #This exception only captures errors of type ValueError
    print('Invalid value')
except ZeroDivisionError: #Exception for the division by 0 error
    print('Age cannot be 0')

