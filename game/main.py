class Player:
    def __init__(self, name,hp,attack,mana):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.mana = mana
    
class Warrior(Player):
    def __init__(self,name, hp, attack,mana):
        super().__init__(name,hp,attack,mana)
        block = block

class Archer(Player):
    def __init__(self,name,hp,attack,mana):
        super().__init__(name,hp,attack,mana)
        double_attack = double_attack

class Mage(Player):
    def __init__(self,name,hp,attack,mana):
        super().__init__(name,hp,attack,mana)
        mana_regen = mana_regen
        fireball = fireball