from Combat import combat
from Enemies import *
from Characters import Warrior,Archer,Mage
from EnemyFactory import *
import os
class Level:
    def __init__(self, player, enemy_factory):
        self.player = player
        self.enemy_factory = enemy_factory
    
    def start(self):
        enemies = self.enemy_factory()
        combat(self.player, enemies)

warrior = Warrior("Warrior",100,10,50,"Block")
archer = Archer("Archer",80,15,10,"Double Attack")
mage = Mage("Mage",100,30,100,"Fireball")
stats = [warrior.stats(),archer.stats(),mage.stats()]
# def refresh_hp(player):
#     player.hp = hp           
def play():
    for i in stats:
        print(f"{i} \n")
    while True:
        INPUT = int(input("CHOOSE YOUR CHAMPION:\n1 - Warrior\n2 - Archer\n3 - Mage\n"))
        if INPUT == 1:
            os.system("cls" if os.name == "nt" else "clear")
            player = warrior
            break
        if INPUT == 2:
            os.system("cls" if os.name == "nt" else "clear")
            player = archer
            break
        if INPUT == 3:
            os.system("cls" if os.name == "nt" else "clear")
            player = mage
            break
        else:
            print("Enter a correct number")
    level1 = Level(player, create_enemies1)
    level2 = Level(player, create_enemies2)
    levels = [level1,level2]
    for index, level in enumerate(levels):
            level.start()
            #refresh_hp(player)
            if index == len(levels) - 1:
                print("We don't have any more levels!")
                break

            ask = input("Would you like to continue? (y/n): ").lower()
            if ask != "y":
                print("Thanks for playing!")
                break