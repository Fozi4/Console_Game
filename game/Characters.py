
class Player:
    def __init__(self, name,hp,attack,mana,ability):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.mana = mana
        self.ability = ability
    def stats(self):
        return f"{self.name} stats: \nhp: {self.hp} \ndmg:{self.attack} \nmana:{self.mana} \nability: {self.ability}"
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, dmg):
        self.hp -= dmg
        
    
    def normal_attack(self, target):
        
        target.take_damage(self.attack)
        return str(f"{self.name} attacks {target.name} for {self.attack} damage!")
    
    def use_ability(self, target):
        pass  
    def __str__(self):
        return f"You've chosen {self.name}"
    
    
class Warrior(Player):
    def __init__(self,name, hp, attack,mana,block):
        super().__init__(name,hp,attack,mana,block)

    
    
class Archer(Player):
    def __init__(self,name,hp,attack,mana,double_attack):
        super().__init__(name,hp,attack,mana,double_attack)
    def use_ability(self, target):
        if self.mana >= 10:
            dmg = self.attack * 2
            print(f"{self.name} uses Double Attack for {dmg} damage!")
            target.take_damage(dmg)
            self.mana -= 10
        else:
            print(f"{self.name} has not enough mana!")

class Mage(Player):
    def __init__(self,name,hp,attack,mana,fireball):
        super().__init__(name,hp,attack,mana,fireball)
    def use_ability(self, target):
        if self.mana >= 20:
            dmg = self.attack + 20
            print(f"{self.name} uses Fireball for {dmg} damage!")
            target.take_damage(dmg)
            self.mana -= 20
        else:
            print(f"{self.name} has not enough mana!")
    



warrior = Warrior("Warrior",100,10,50,"Block")

archer = Archer("Archer", 90,20,70,"Double Attack")

mage = Mage("Mage", 60,40,100,"Fireball")

stats = [warrior.stats(),archer.stats(),mage.stats()]
for i in stats:
    print(f"{i} \n")

# choose = int(input("Choose your character from 0 to 2:"))
# characters = [warrior, archer, mage]
# character=characters[choose]
# print(character)

