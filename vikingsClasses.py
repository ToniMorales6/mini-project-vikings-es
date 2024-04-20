import random

''' 
    Team: Antonio Morales, Maksym Vaskyn, Iván Seldas, Marc Cabré
'''

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
        super().__init__(health, strength)
        self.name = name
    
    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

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

class War():
    def __init__(self):
        self.vikingArmy = list()
        self.saxonArmy = list()

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking_selected = random.choice(self.vikingArmy)
        saxon_selected = random.choice(self.saxonArmy)

        result = saxon_selected.receiveDamage(viking_selected.attack())

        if saxon_selected.health <= 0:
            self.saxonArmy.remove(saxon_selected)
        
        return result

    
    def saxonAttack(self):
        viking_selected = random.choice(self.vikingArmy)
        saxon_selected = random.choice(self.saxonArmy)

        result = viking_selected.receiveDamage(saxon_selected.attack())
        
        if viking_selected.health <= 0:
            self.vikingArmy.remove(viking_selected)
        
        return result


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


#yop
class War2:
    def __init__(self):
        self.vikingArmy = list()
        self.saxonArmy = list()

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking_selected = random.choice(self.vikingArmy)
        saxon_selected = random.choice(self.saxonArmy)

        result = saxon_selected.receiveDamage(viking_selected.attack())

        if saxon_selected.health <= 0:
            self.saxonArmy.remove(saxon_selected)
        
        return result

    
    def saxonAttack(self):
        viking_selected = random.choice(self.vikingArmy)
        saxon_selected = random.choice(self.saxonArmy)

        result = viking_selected.receiveDamage(saxon_selected.attack())
        print(len(self.vikingArmy))
        if viking_selected.health <= 0:
            self.vikingArmy.remove(viking_selected)
        
        return result


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
