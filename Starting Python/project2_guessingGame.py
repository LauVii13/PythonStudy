from random import randint


secret_number = randint(0, 9)
guess_limit = 3
i = 1

while i <= guess_limit:
    answer = int(input('Guess(0-9): '))
    
    if answer == secret_number:
        print('You Won!')
        break
    i += 1

else: #in python, while can have a else tag -> if the while was finished completely, without a break or something like that, the 'else' will run
    print("Sorry, you failed!")
