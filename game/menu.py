from Characters import *
import os
import lvls 
archer = Archer("Archer",80,15,10,"Double Attack")
mage = Mage("Mage",60,20,70,"Fireball")
warrior = Warrior("Warrior",100,10,50,"Block")

class Level_expirience:
    def __init__(self, exp):
        self.exp = exp
    def exp_increase(self,expa):
        self.exp +=expa
    def exp_decrease(self,expa):
        if self.exp<=0:
            return
        if self.exp - expa <=0:
            return
        self.exp -= expa


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
            lvls.play()
            _choose = False
        elif choice == "2":
            print(stats(warrior,archer,mage))
            print("Right now there is no upgrades here  :(")
            input("Press enter to return.....")
        elif choice == "3":
            _choose = False
        else:
            print("Enter a correct number!")



def stats(character1, character2, character3):
    result = ""
    result = "Current expirience:\n"
    result += "-" * 90 + "\n"
    result += f"{character1.name:<30} | {character2.name:<30} | {character3.name:<30}\n"
    result += "-" * 90 + "\n"
    result += f"HP:    {character1.hp:<23} | HP:    {character2.hp:<23} | HP:    {character3.hp:<23}\n"
    result += f"DMG:   {character1.attack:<23} | DMG:   {character2.attack:<23} | DMG:   {character3.attack:<23}\n"
    result += f"MANA:  {character1.mana:<23} | MANA:  {character2.mana:<23} | MANA:  {character3.mana:<23}\n"
    result += f"ABILITY:{character1.ability:<22} | ABILITY:{character2.ability:<22} | ABILITY:{character3.ability:<22}\n"
    result += "-" * 90 + "\n"
    return result

if __name__ == "__main__":
    main_menu()