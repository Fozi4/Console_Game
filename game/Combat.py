import os
from Characters import Player
from Enemies import Enemy
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
        print("Choose which enemy to attack")
        
        for idx, enemy in enumerate(enemies):
            print(f"[{idx}] {enemy.name} - HP: {enemy.hp}") 
             
        choose = int(input("Enter enemy number: "))      
        target = targets(enemies, choose)
        if target is None or not target.is_alive():
            print("Invalid or dead target.")
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
            if enemy.is_alive():
                if turn % 2 == 0:
                    messages.append(enemy.enemy_ability(player))
                else:
                    messages.append(enemy.enemy_attack(player))
        
        if not player.is_alive():
            print(f"{player.name} is defeated!")
            break
        
        turn += 1
        os.system("cls" if os.name == "nt" else "clear")
