import readchar
import os

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGTH = 15

my_position = [6, 3]

while True:

    #   Draw Map
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coordinate_y in range(MAP_HEIGTH):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
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
