import os

#VARIABLES
n1 = 0
n2 = 1

#ASKING AGAIN IF THE INPUT IS 0
while True:
    user_number = int(input('\nHow many numbers of the Fibonacci Sequence do you wanna display ?: '))
    os.system('clear')
    print('\nPlease! Enter a positive number!')
    if user_number > 0:
        break

os.system('clear')

#DISPLAYING ONLY ONE NUMBER OF THE SEQUENCE
if user_number == 1:
    print('\nFibonacci sequence: {}'.format(n1))

#DISPLAYING X NUMBERS OF THE SEQUENCE
else:
    print('\nFibonacci sequence: ')
    for x in range(user_number):
        print('-', n1)
        next = n1 + n2
        
        n1 = n2
        n2 = next