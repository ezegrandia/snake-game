import readchar
import os
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGTH = 15

my_position = [6, 3]
map_fruits = []

for x in range(10):
    fruit_position = []
    x = random.randint(0, MAP_WIDTH)
    fruit_position.append(x)
    y = random.randint(0, MAP_HEIGTH)
    fruit_position.append(y)
    map_fruits.append(fruit_position)

while True:

    #   Draw Map
    print("+" + "-" * (MAP_WIDTH * 3) + "+")
    for coordinate_y in range(MAP_HEIGTH):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            fruit_in_cell = None
            for fruit in map_fruits:
                if fruit[POS_X] == coordinate_x and fruit[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    fruit_in_cell = fruit
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if fruit_in_cell:
                    map_fruits.remove(fruit_in_cell)
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    # Ask user where he wants to move
    print("Utilice \"WASD\" para moverse \n\"Q\" para salir")
    direction = readchar.readchar()

    if direction.lower() == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGTH
    elif direction.lower() == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGTH
    elif direction.lower() == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction.lower() == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction.lower() == "q":
        break

    os.system("clear")
