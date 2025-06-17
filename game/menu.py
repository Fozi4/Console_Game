from Combat import *
import Characters
import os
import Combat



# while _choose:
#     os.system("cls" if os.name == "nt" else "clear")
#     print("-----------------------")
#     print("Play\nUpgrades\nExit")
#     print("-----------------------")
#     print("1 - PLAY; 2 - UPGRADES; 3 - EXIT.")
#     print("-----------------------")
#     INPUT = input("::-->")
#     if INPUT == 1:
#         character_chooseing()
#         _choose = False
        
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    print("--------------------------")
    print("        MAIN MENU         ")
    print("--------------------------")
    print("1         PLAY")
    print("2       UPGRADES")
    print("3         EXIT")
    print("--------------------------")
        
def main_menu():
    _choose = True
    while _choose:
        clear_screen()
        show_menu()
        
        choice = input("------> ")
        
        if choice == "1":
            Combat.character_chooseing()
            # map_data = create_map(20, 20)
            # map_data[2][2] = 'P'  # игрок в центре
            # game_map(map_data)


            _choose = False
        elif choice == "2":
            print("Right now there is nothing here :(")
        elif choice == "3":
            _choose = False
        else:
            print("Enter a correct number!")



# def create_map(width, height):
#     return [['▇' for _ in range(width)] for _ in range(height)]

# def game_map():





# def game_map(map_data):
#     for row in map_data:
#         print(" ".join(row))


if __name__ == "__main__":
    main_menu()