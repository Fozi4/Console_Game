from random import randint
from Characters import Player,Warrior,Archer,Mage
from Enemies import Enemy
import os

#--------------------Characters-------------------------------#
warrior = Warrior("Warrior",100,10,50,"Block")
archer = Archer("Archer",80,15,10,"Double Attack")
mage = Mage("Mage",60,20,70,"Fireball")
#-------------------Enemies--------------------------------#
enemy = Enemy("Ork",50,5,10,"bite")
#-------------------------------------------------------------#
_choose = True
messages = []
messages.append("-----ACTIONS------")
# _characters=[]
# _characters.append(warrior,archer,mage)

def show_messeges(messeges):
        for i in messages:
            print(" "*50+i)







def combat(player, enemy):
    turn = 1
    while player.is_alive() and enemy.is_alive():
        print(f"\n------------ Turn {turn} ---------") 
        print(show_messeges(messages))

        print(f"{player.name} HP: {player.hp}, Mana: {player.mana}"+"\n")
        print("\n" + " "*10+"VS"+"\n")
        print(f"{enemy.name} HP: {enemy.hp}")
        

        action = input("Choose action: (1) Attack (2) Ability: ")
        if action == "1":
            
            messages.append(player.normal_attack(enemy))
        elif action == "2":
            player.use_ability(enemy)
        else:
            print("Invalid choise< ti dolboeb")

        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")
            break
        
        
        enemy.normal_attack(player)
        if not player.is_alive():
            print(f"{player.name} is defeated!")
            break
        
        turn += 1
        os.system("cls" if os.name == "nt" else "clear")


while _choose:
    INPUT = int(input("CHOOSE YOUR CHAMPION:\n1 - Warrior\n2 - Archer\n3 - Mage\n"))
    if INPUT == 1:
        os.system("cls" if os.name == "nt" else "clear")
        combat(warrior, enemy)
        _choose = False
    if INPUT == 2:
        os.system("cls" if os.name == "nt" else "clear")
        combat(archer, enemy)
        _choose = False
    if INPUT == 3:
        os.system("cls" if os.name == "nt" else "clear")
        combat(mage, enemy)
        _choose = False
    else:
        print("Enter a correct number")