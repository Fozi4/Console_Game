from Characters import Player
class Enemy(Player):
    def __init__(self,name, hp, attack,mana,ability):
        super().__init__(name,hp,attack,mana,ability)
    
    def enemy_attack(self, target):
        
        target.take_damage(self.attack)
        return str(f"{self.name} attacks {target.name} for {self.attack} damage!")
class Ork(Enemy):
    def __init__(self,name,hp,attack,mana,bite):
        super().__init__(name,hp,attack,mana,"bite")
    def enemy_ability(self,target):
        if self.mana >= 10:
            dmg = 8
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses bite for {dmg} damage!")
        else:
            return self.enemy_attack(target)

class Goblin(Enemy):
    def __init__(self,name,hp,attack,mana,knife_trow):
        super().__init__(name,hp,attack,mana,"knife trow")
    def enemy_ability(self,target):
        if self.mana >= 10:
            dmg = self.attack + 5
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses knife trow for {dmg} damage!")
        else:
            return self.enemy_attack(target)

