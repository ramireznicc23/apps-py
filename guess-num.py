import random
import os

title = 'Welcome to Guess My Number v1.0'

print(title)
print('-' * len(title))
print('\nI am thinking in a number between 1 and 100. Try to guess it ;)')
input('\nPress Enter to begin ...')

number = random.randint(1, 100)

number_guessed = False

tries = 0

while number_guessed == False :
    os.system('clear')
    number_user = int(input('\nWhat is the number I am thinking of ?: '))
    
    if number_user > 100 :
        print('\nThe number was between 1 and 100!')
        print('\nBye!')
        break

    elif number_user < number :
        os.system('clear')
        input('\nToo low! Try again! Press [Enter] to continue ...')
        tries += 1    
    
    elif number_user > number :
        os.system('clear')
        input('\nToo high! Try again! Press [Enter] to continue ...')
        tries += 1

    else :
        os.system('clear')
        number_guessed = True
        print('\nYes! You have guessed the number! Congratulations!')
        str(print('\nYou did it in', tries, 'tries.'))
