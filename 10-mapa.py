import readchar
import os
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGTH = 15
NUM_OF_MAP_FRUITS = 10

my_position = [6, 3]
tail_length = 0
tail = []
map_fruits = []

# Main loop
while True:
    # Generate random fruits on the map
    while len(map_fruits) < NUM_OF_MAP_FRUITS:
        new_fruit_position = [random.randint(
            0, MAP_WIDTH-1), random.randint(0, MAP_HEIGTH-1)]
        if new_fruit_position not in map_fruits and new_fruit_position != my_position:
            map_fruits.append(new_fruit_position)
    #   Draw Map
    print("\nUtilice \"WASD\" para moverse \n\"Q\" para salir\n If you collide with your tail you lose\n")
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
            for tail_unit in tail:
                if tail_unit[POS_X] == coordinate_x and tail_unit[POS_Y] == coordinate_y:
                    char_to_draw = "@"
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if fruit_in_cell:
                    map_fruits.remove(fruit_in_cell)
                    tail_length += 1
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    # Ask user where he wants to move
    print("SCORE: {}".format(tail_length))
    direction = readchar.readchar()

    if direction.lower() == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGTH
        if my_position in tail:
            print("GAME OVER")
            break
    elif direction.lower() == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGTH
        if my_position in tail:
            print("GAME OVER")
            break
    elif direction.lower() == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
        if my_position in tail:
            print("GAME OVER")
            break
    elif direction.lower() == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
        if my_position in tail:
            print("GAME OVER")
            break
    elif direction.lower() == "q":
        print("Q > Quit Game")
        break

    os.system("clear")
