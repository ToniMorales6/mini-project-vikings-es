import random

# Soldier


class Soldier:
    def __init__(self, health: float, strength: float):
        self.health = health
        self.strength = strength

    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        return 

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__ini__(health, strength)
        self.name = name

    def attack(self):
        print("Odin Owns You All!")
    
    def battleCry(self):
        print ('Odin os posee a todos')

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            print(f'{self.name} ha recibido {damage} puntos de daño')
        else:
            print(f'{self.name} ha muerto en acto de combate')

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return ("A Saxon has died in combat")

# Davicente
"""
class War():
    def __init__(self):
        # your code here

    def addViking(self, viking):
        # your code here
    
    def addSaxon(self, saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here
    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass

#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass
    """