from Combat import combat
from Enemies import *
from Characters import Player,Warrior,Archer,Mage
import os
class Level:
    def __init__(self,player,enemies):
        self.player = player
        self.enemies = enemies
    
    def start(self):
        combat(self.player, self.enemies)

warrior = Warrior("Warrior",100,10,50,"Block")
archer = Archer("Archer",80,15,10,"Double Attack")
mage = Mage("Mage",100,30,100,"Fireball")
stats = [warrior.stats(),archer.stats(),mage.stats()]
for i in stats:
    print(f"{i} \n")
ork = Ork("Ork",50,5,10,"bite")
goblin = Goblin("Goblin",80,10,20,"Knife trow")
enemies1 = [ork,ork]
enemies2 = [ork,goblin]
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
level1 = Level(player,enemies1)
level2 = Level(player, enemies2)
level2.start()