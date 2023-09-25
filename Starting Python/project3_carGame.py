# Enter a code that if you type 'help' will show the commands, 'start' will start the car, 'stop' will stop the car and 'quit' will terminate the program.
# But if the car has already started and you type 'start' again, another message needs to be shown, same rule for 'stop'.

from operator import truediv


command = ""
started = False

print('Type Help to start\n')

while True: # While True means this block of code is going to get executed repeatedly until something breaks it
    command = input('> ').lower()
    
    #Help command
    if  command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
            ''')
    
    #Start command
    elif command == 'start':
        if started:
            print('The car is already started\n')
        else:
            print('Car started...\n')
            started = True
            
            
    #Stop command
    elif command == 'stop':
        if not started:
            print('The car is already stopped\n')
        else:
            started = False
            print('Car stopped.\n')
            
    #Quit command
    elif command == 'quit':
        break
    
    else:
        print("Sorry, I don't understand that!\n") 

