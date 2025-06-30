from Characters import Player
class Enemy(Player):
    def __init__(self,name, hp, attack,mana,ability):
        super().__init__(name,hp,attack,mana,ability)
    
    def enemy_attack(self, target):
        
        target.take_damage(self.attack)
        return str(f"{self.name} attacks {target.name} for {self.attack} damage!")
class Ork(Enemy):
    def __init__(self,name,hp,attack,mana,bite):
        super().__init__(name,hp,attack,mana,"Bite")
    def enemy_ability(self,target):
        if self.mana >= 10:
            dmg = 7
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses Bite for {dmg} damage!")
        else:
            return self.enemy_attack(target)

class Goblin(Enemy):
    def __init__(self,name,hp,attack,mana,knife_trow):
        super().__init__(name,hp,attack,mana,"Knife trow")
    def enemy_ability(self,target):
        if self.mana >= 10:
            dmg = self.attack + 3
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses Knife trow for {dmg} damage!")
        else:
            return self.enemy_attack(target)

class Dark_Mage(Enemy):
    def __init__(self,name,hp,attack,mana,fireball):
        super().__init__(name,hp,attack,mana,"Fireball")
    def enemy_ability(self,target):
        if self.mana >= 15:
            dmg = self.attack + 5
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses Fireball trow for {dmg} damage!")
        else:
            return self.enemy_attack(target)