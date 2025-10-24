'''
1h31m https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f

Build a program which when you input:
asd: Output I dont understand
start: Car started...
Stop: Car stopped
Quit: Quits program

'''
user_input = ""
car_status = ""

while True:
    user_input = input("Enter Instruction: ").lower()
    if user_input == 'start':
        if car_status == 'started':
            print('Car is already started')
        else:
            car_status = 'started'
            print('Car started!')
    elif user_input == 'stop':
        if car_status == 'stopped':
            print('Car is already stopped')
        else:
            car_status = 'stopped'
            print('Car stopped!')
    elif user_input == 'help':
        print(
"""Start: Car started...
Stop: Car stopped'
Quit: Quits program""")
    elif user_input == 'quit':
        break
    else:
       print('Not understood')