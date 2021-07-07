import os

print('Welcome to Shopping List v1.0 by Nico.')

lista_super = []

lista = True

while lista == True :
    item_usuario = input('\nWhat do you want to add to the list? -Press [Q] to finish- : ')

    if item_usuario == 'Q' :
        lista = False
    
    else :
        if item_usuario in lista_super:
                os.system('clear')
                print('\n{} is already on the list!'.format(item_usuario))
                continuar = input('\nPress [Enter] to continue or [Q] to finish ... ')
                if continuar == 'Q' :
                    break
                os.system('clear')
        
        else :
            os.system('clear')
            confirmacion = input('\nAre you sure that you want to add {} to the list ? [Y/N]: '.format(item_usuario))
        
            if confirmacion == 'Y' : 
                lista_super.append(item_usuario)
                os.system('clear')
                print('\nYou added {} to the list.'.format(item_usuario))
                continuar = input('\nPress [Enter] to continue or [Q] to finish ...')
                if continuar == 'Q' :
                    break
                os.system('clear')
        
            else:
                os.system('clear')
                print('\n{} has not been added to the list.'.format(item_usuario))
                continuar = input('\nPress [Enter] to continue or [Q] to finish ... ')
                if continuar == 'Q' :
                    break
                os.system('clear')
    
os.system('clear')
print('\nYour list is done!: \n')

for item in lista_super:
    print('-', item)

print('\nThanks to use Shopping List v1.0 by Nico.')