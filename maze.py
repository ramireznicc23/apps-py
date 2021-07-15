import readchar
import os
import random

os.system('clear')

#CONSTANTS
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_MAP_OBJ = 11

#VARIABLES
my_position = [3, 1]
map_objects = []
tail_lenght = 0
tail = []

game_on = True

#GENERATE RANDOM OBJECTS
while len(map_objects) < NUM_MAP_OBJ:
    new_position = [random.randint(0, 19), random.randint(0, 14)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

#MAIN LOOP
while game_on == True: 
    #MAP DRAW
    print('+' + '-' * MAP_WIDTH * 3 + '+')

    for coord_y in range(MAP_HEIGHT):
        print('|', end='')
        for coord_x in range(MAP_WIDTH):

            char_to_draw = ' '

            for map_object in map_objects:
                if my_position == map_object:
                    map_objects.remove(map_object)
                    tail_lenght += 1

                elif map_object[POS_X] == coord_x and map_object[POS_Y] == coord_y:
                    char_to_draw = '*'
            
            for tail_piece in tail:
                if tail_piece[POS_X] == coord_x and tail_piece[POS_Y] == coord_y:
                    char_to_draw = '@'
                    
            if my_position[POS_X] == coord_x and my_position[POS_Y] == coord_y:
                char_to_draw = '@'

            if len(map_objects) == 0:
                while len(map_objects) < NUM_MAP_OBJ:
                    new_position = [random.randint(0, 19), random.randint(0, 14)]

                    if new_position not in map_objects and new_position != my_position:
                        map_objects.append(new_position)
                
            print(' {} '.format(char_to_draw), end="")

        print('|')

    print('+' + '-' * MAP_WIDTH * 3 + '+')
    print('\nYour score: {}'.format(tail_lenght))

    #USER MOVING
    print('\nPress [W]⬆ [A]⬅️ [S]⬇️ [D]➡️  to move around the map.\nPress [Q]✖️  to quit.\n')
    direction = readchar.readchar()

    if direction == 'w':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] -= 1
    elif direction == 's':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] += 1
    elif direction == 'a':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] -= 1
    elif direction == 'd':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] += 1
    elif direction == 'q':
        break

    #REAPERING ON THE OTHER SIDE OF THE MAP
    if my_position[POS_Y] >= MAP_HEIGHT:
        my_position[POS_Y] = 0
    elif my_position[POS_Y] < 0:
        my_position[POS_Y] = 14
    elif my_position[POS_X] >= MAP_WIDTH:
        my_position[POS_X] = 0
    elif my_position[POS_X] < 0:
        my_position[POS_X] = 19

    os.system('clear')
    
    for item_tail in tail:
        if item_tail == my_position:
            game_on = False

            print('\nYou lose :( \n\nYour final score was: {}'.format(tail_lenght))
