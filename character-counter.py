import os
import string

title = '\nWelcome to Text Disassembler v1.0 by ramireznicc.'

print(title)
print('*' * (len(title) - 1))
print('\nWith this software you will be able to disassemble a text that you write, telling you the number of characters that compose it. ')
input('\nPress[Enter] to begin ...')

os.system('clear')

user_text = input('\nEnter your text: ')

VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

amount_letters = 0
amount_upcase = 0
amount_lowcase = 0
amount_vowels = 0
amount_consonants = 0
amount_spaces = 0
amount_points = 0
amount_commas = 0

for letter in user_text:
    if letter in string.ascii_letters:
        amount_letters += 1
    if letter in string.ascii_uppercase:
        amount_upcase += 1
    if letter in string.ascii_lowercase:
        amount_lowcase += 1

for letter in user_text:
    if letter in VOWELS:
        amount_vowels += 1
    elif letter == ' ':
        amount_spaces += 1
    elif letter == '.':
        amount_points += 1
    elif letter == ',':
        amount_commas += 1
    else:
        amount_consonants  += 1


os.system('clear')
print('\nIn the text {} I have found: '.format(user_text))

print('\n{} letters.'.format(amount_letters))
print('{} capital letters.'.format(amount_upcase))
print('{} lower case.'.format(amount_lowcase))
print('{} vowels.'.format(amount_vowels))
print('{} consonants.'.format(amount_consonants))
print('{} spaces.'.format(amount_spaces))
print('{} points.'.format(amount_points))
print('{} commas.'.format(amount_commas))
