import os

title = '\nWelcome to Shopping List v1.0 by Nico.'
print(title)
print('*' * (len(title) - 1))

shopping_list = []

list = True

while list == True :
    user_item = input('\nWhat do you want to add to the list? -Press [Q] to finish- : ')

    if user_item == 'Q' :
        list = False
    
    else :
        if user_item in shopping_list:
                os.system('clear')
                print('\n{} is already on the list!'.format(user_item))
                ok = input('\nPress [Enter] to continue or [Q] to finish ... ')
                if ok == 'Q' :
                    break
                os.system('clear')
        
        else :
            os.system('clear')
            confirmation = input('\nAre you sure that you want to add {} to the list ? [Y/N]: '.format(user_item))
        
            if confirmation == 'Y' : 
                shopping_list.append(user_item)
                os.system('clear')
                print('\nYou added {} to the list.'.format(user_item))
                ok = input('\nPress [Enter] to continue or [Q] to finish ...')
                if ok == 'Q' :
                    break
                os.system('clear')
        
            else:
                os.system('clear')
                print('\n{} has not been added to the list.'.format(user_item))
                ok = input('\nPress [Enter] to continue or [Q] to finish ... ')
                if ok == 'Q' :
                    break
                os.system('clear')
    
os.system('clear')
print('\nYour list is done!: \n')

for item in shopping_list:
    print('-', item)

print('\nThanks to use Shopping List v1.0 by Nico.')