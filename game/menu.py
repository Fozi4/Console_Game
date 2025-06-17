from Combat import *
import Characters
import os
import Combat

archer = Archer("Archer",80,15,10,"Double Attack")
mage = Mage("Mage",60,20,70,"Fireball")
warrior = Warrior("Warrior",100,10,50,"Block")
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
            print(stats(warrior,archer,mage))
            print("Right now there is no upgrades here  :(")
            input("Press enter to return.....")
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






# def stats(character1,character2,character3):
#         return print(f"{character1.name} stats:     |     {character2.name} stats:     |     {character3.name} stats:\n
#                      f"hp: {character1.hp} hp: {character2.hp} hp: {character3.hp}\n
#                      f"dmg:{character1.attack} dmg:{character2.attack} dmg:{character3.attack}\n
#                      f"mana:{character1.mana} mana:{character2.mana} mana:{character3.mana} \n
#                      f"ability: {character1.ability} ability: {character2.ability} ability: {character3.ability}\n"
    



def stats(character1, character2, character3):
    result = ""
    result += f"{character1.name:<30} | {character2.name:<30} | {character3.name:<30}\n"
    result += "-" * 90 + "\n"
    result += f"HP:    {character1.hp:<23} | HP:    {character2.hp:<23} | HP:    {character3.hp:<23}\n"
    result += f"DMG:   {character1.attack:<23} | DMG:   {character2.attack:<23} | DMG:   {character3.attack:<23}\n"
    result += f"MANA:  {character1.mana:<23} | MANA:  {character2.mana:<23} | MANA:  {character3.mana:<23}\n"
    result += f"ABILITY:{character1.ability:<22} | ABILITY:{character2.ability:<22} | ABILITY:{character3.ability:<22}\n"
    return result

if __name__ == "__main__":
    main_menu()