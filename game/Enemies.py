from Characters import Player


class Enemy(Player):
    def __init__(self, name, hp, attack, mana, ability, exp):
        super().__init__(name, hp, attack, mana, ability)
        self.exp = exp

    def enemy_attack(self, target):

        target.take_damage(self.attack)
        return str(f"{self.name} attacks {target.name} for {self.attack} damage!")


class Ork(Enemy):
    def __init__(self, name, hp, attack, mana, exp):
        super().__init__(name, hp, attack, mana, "Bite", exp)

    def enemy_ability(self, target):
        if self.mana >= 10:
            dmg = 7
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses Bite for {dmg} damage!")
        else:
            return self.enemy_attack(target)


class Goblin(Enemy):
    def __init__(self, name, hp, attack, mana, exp):
        super().__init__(name, hp, attack, mana, "Knife trow", exp)

    def enemy_ability(self, target):
        if self.mana >= 10:
            dmg = self.attack + 3
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses Knife trow for {dmg} damage!")
        else:
            return self.enemy_attack(target)


class Dark_Mage(Enemy):
    def __init__(self, name, hp, attack, mana, exp):
        super().__init__(name, hp, attack, mana, "Fireball", exp)

    def enemy_ability(self, target):
        if self.mana >= 15:
            dmg = self.attack + 5
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses Fireball trow for {dmg} damage!")
        else:
            return self.enemy_attack(target)
