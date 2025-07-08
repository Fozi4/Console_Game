
class Player:
    def __init__(self, name, hp, attack, mana, ability):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.mana = mana
        self.ability = ability
        self.exp = 0
        self.lvl = 1

    def stats(self):
        return f"{self.name} stats: \nhp: {self.hp} \ndmg:{self.attack} \nmana:{self.mana} \nability: {self.ability}"

    def is_alive(self):
        return self.hp > 0

    def gain_exp(self, amount_of_exp):
        self.exp += amount_of_exp
        print(f"{self.name} gained {amount_of_exp} EXP. Total: {self.exp}")
        lvl_up = 100

        if self.exp >= lvl_up * self.lvl:
            self.lvl += 1
            print(f"You leveled up to {self.lvl}")
            self.hp += 10
            self.attack += 2
            self.mana += 5
            print(f"""New stats: 
                    HP: {self.hp}
                    Attack: {self.attack}
                    Mana: {self.mana}    """)

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
    def __init__(self, name, hp, attack, mana, block):
        super().__init__(name, hp, attack, mana, block)


class Archer(Player):
    def __init__(self, name, hp, attack, mana, double_attack):
        super().__init__(name, hp, attack, mana, double_attack)

    def use_ability(self, target):
        if self.mana >= 10:
            dmg = self.attack * 2
            target.take_damage(dmg)
            self.mana -= 10
            return str(f"{self.name} uses Double Attack for {dmg} damage!")
        else:
            return str(f"{self.name} has not enough mana!")


class Mage(Player):
    def __init__(self, name, hp, attack, mana, fireball):
        super().__init__(name, hp, attack, mana, fireball)

    def use_ability(self, target):
        if self.mana >= 20:
            dmg = self.attack + 20
            target.take_damage(dmg)
            self.mana -= 20
            return str(f"{self.name} uses Fireball for {dmg} damage!")
        else:
            return str(f"{self.name} has not enough mana")
