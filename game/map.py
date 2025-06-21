# from lvls import *
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def draw_map(map_data):
    for row in map_data:
        print("".join(row))

def create_map(width, height):
    return [['▓' for _ in range(width)] for _ in range(height)]

def generation(player_x, player_y):
    game_map = create_map(40, 20)

    for i in range(len(game_map)):
        game_map[i][0] = '█'
        game_map[i][-1] = '█'
    for j in range(len(game_map[0])):
        game_map[0][j] = '▇'
        game_map[-1][j] = '▇'
    game_map[player_y][player_x] = 'P'
    game_map[3][6] = 'E'

    draw_map(game_map)

player_x = 2
player_y = 4

clear_screen()
generation(player_x, player_y)

while True:
    INPUT = input("---->").lower()
    
    if INPUT == "w" and player_y > 1:
        player_y -= 1
    elif INPUT == "s" and player_y < 18:
        player_y += 1
    elif INPUT == "a" and player_x > 1:
        player_x -= 1
    elif INPUT == "d" and player_x < 38:
        player_x += 1
    else:
        print("Enter a correct value.")
        continue

    clear_screen()
    generation(player_x, player_y)
