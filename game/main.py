class Player:
    def __init__(self, name,hp,attack,mana,ability):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.mana = mana
        self.ability = ability
    def stats(self):
        return f"{self.name} stats: \nhp: {self.hp} \ndmg:{self.attack} \nmana:{self.mana} \nability: {self.ability}"
    def take_damage(self,dmg):
        if self.hp - dmg <=0:
            return "You died!!!"
        
        self.hp -=dmg
        return f"Remaining health {self.hp}"
    

    
    
class Warrior(Player):
    def __init__(self,name, hp, attack,mana,block):
        super().__init__(name,hp,attack,mana,block)
    
    
class Archer(Player):
    def __init__(self,name,hp,attack,mana,double_attack):
        super().__init__(name,hp,attack,mana,double_attack)

class Mage(Player):
    def __init__(self,name,hp,attack,mana,fireball):
        super().__init__(name,hp,attack,mana,fireball)
    



warrior = Warrior("0-Warrior",100,10,50,"Block")

archer = Archer("1-Archer", 90,20,70,"Double Attack")

mage = Mage("2-Mage", 60,40,100,"Fireball")

stats = [warrior.stats(),archer.stats(),mage.stats()]
for i in stats:
    print(f"{i} \n")

choose = input("Choose your character from 0 to 2:")
characters = [warrior, archer, mage]
character=characters[choose]
print(character)



