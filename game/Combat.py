from random import randint
from Characters import Player,Warrior,Archer,Mage
from Enemies import Enemy
import os
import menu
from menu import *
from menu import Level_expirience

expirience = Level_expirience(0)
#--------------------Characters-------------------------------#
warrior = Warrior("Warrior",100,10,50,"Block")
archer = Archer("Archer",80,15,10,"Double Attack")
mage = Mage("Mage",60,20,70,"Fireball")
#-------------------Enemies--------------------------------#
enemy = Enemy("Ork",50,5,10,"bite")
enemy1 = Enemy("Ork",50,5,10,"bite")
enemies = [enemy,enemy1]
#-------------------------------------------------------------#
messages = []
messages.append("-----ACTIONS------")

def show_messeges(messeges):
        for i in messages:
            print(" "*50+i)

def targets(enemies, index_str):
    try:
        index = int(index_str)
        if 0 <= index < len(enemies):
            return enemies[index]
        else:
            return None
    except ValueError:
        return None
  
        
def _is_combat_finished_():
     for enemy in enemies:
            if len(enemies)<=0:
                expirience.exp_increase(40)
                print("+40 exp")
                input("press enter...")
                main_menu()

def enemies_alive(enemies):
    return any(enemy.is_alive() for enemy in enemies)

def combat(player, enemies):
    turn = 1
    while player.is_alive() and enemies_alive(enemies):
       
        print(f"\n------------ Turn {turn} ---------") 
        show_messeges(messages)

        print(f"{player.name} HP: {player.hp}, Mana: {player.mana}"+"\n")
        print("\n" + " "*10+"VS"+"\n")
        for enemy in enemies:
            print(f"{enemy.name} HP: {enemy.hp}")

        action = input("Choose action: (1) Attack (2) Ability: ")
        for idx, enemy in enumerate(enemies):
                print(f"[{idx}] {enemy.name} - HP: {enemy.hp}")
        choose = int(input("Enter enemy number"))
        target = targets(enemies, choose)
        if target is None:
            print("Invalid target input")
            continue
            
        if action == "1":
            messages.append(player.normal_attack(target))
        elif action == "2":
            messages.append(player.use_ability(target))
        else:
            print("Invalid choise< ti dolboeb")

        if not enemies_alive(enemies):
            for enemy in enemies:
                print(f"{enemy.name} is defeated!")
                
            break
        
        
        for enemy in enemies:
            if not enemy.is_alive():
                enemies.remove(enemy)  
                
        

            messages.append(enemy.normal_attack(player))
        if not player.is_alive():
            print(f"{player.name} is defeated!")
            break
        
        turn += 1
        os.system("cls" if os.name == "nt" else "clear")

def character_chooseing():
    _choose = True
    while _choose:
        INPUT = int(input("CHOOSE YOUR CHAMPION:\n1 - Warrior\n2 - Archer\n3 - Mage\n4 - MAIN MENU\n-----> "))
        if INPUT == 1:
            menu.clear_screen()
            return combat(warrior, enemies)
            _choose = False
            break
        if INPUT == 2:
            menu.clear_screen()
            return combat(archer, enemies)
            _choose = False
            break                                 #Was created a function clear_screen() 
        if INPUT == 3:
            menu.clear_screen()
            return combat(mage, enemies)
            _choose = False
            break
        if INPUT == 4:
            menu.clear_screen()
            return menu.main_menu()
            _choose = False
            break
        else:
            print("Enter a correct number")