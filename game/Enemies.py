from Characters import Player
class Enemy(Player):
    def __init__(self,name, hp, attack,mana,ability):
        super().__init__(name,hp,attack,mana,ability)
        
    def stats(self):
        return f"{self.name} stats: \nhp: {self.hp} \ndmg:{self.attack} \nmana:{self.mana} \nability:{self.ability}"
enemy = Enemy("Ork",50,5,10,"bite")
enemy1=Enemy("Ork",50,5,10,"bite")
stats = [enemy.stats()]
for i in stats:
    print(f"{i} \n")

