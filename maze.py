import readchar
import os

#CHARACTER POSITION
POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

while True: 

#MAP DRAW
    print('+' + '-' * MAP_WIDTH * 3 + '+')

    for coord_y in range(MAP_HEIGHT):
        print('|', end='')
        for coord_x in range(MAP_WIDTH):
            if my_position[POS_X] == coord_x and my_position[POS_Y] == coord_y:
                print (' @ ', end='')
            else:
                print('   ', end='')
        print('|')

    print('+' + '-' * MAP_WIDTH * 3 + '+')

#USER MOVING
    print('\nPress [W] [A] [S] [D] to move around the map.\nPress [Q] to quit.\n')
    direction = readchar.readchar()

    if direction == 'w':
        my_position[POS_Y] -= 1
    elif direction == 's':
        my_position[POS_Y] += 1
    elif direction == 'a':
        my_position[POS_X] -= 1
    elif direction == 'd':
        my_position[POS_X] += 1
    elif direction == 'q':
        break

#REAPERING ON THE OTHER SIDE OF THE MAP
    if my_position[POS_Y] >= MAP_HEIGHT:
        my_position[POS_Y] = 0
    elif my_position[POS_Y] < 0:
        my_position[POS_Y] = 14
    
    if my_position[POS_X] >= MAP_WIDTH:
        my_position[POS_X] = 0
    elif my_position[POS_X] < 0:
        my_position[POS_X] = 19
    
    os.system('clear')
