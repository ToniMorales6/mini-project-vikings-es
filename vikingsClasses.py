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
        id_viking = random.randrange(len(self.vikingArmy)-1)
        id_saxon = random.randrange(len(self.saxonArmy)-1)

        viking_selected = self.vikingArmy[id_viking]
        saxon_selected = self.saxonArmy[id_saxon]

        result = saxon_selected.receiveDamage(viking_selected.attack())

        if "died in combat" in result:
            self.saxonArmy.pop(id_saxon)
        
        return result

    
    def saxonAttack(self):
        id_viking = random.randrange(len(self.vikingArmy)-1)
        id_saxon = random.randrange(len(self.saxonArmy)-1)

        viking_selected = self.vikingArmy[id_viking]
        saxon_selected = self.saxonArmy[id_saxon]

        result = viking_selected.receiveDamage(saxon_selected.attack())

        if "died in combat" in result:
            self.vikingArmy.pop(id_viking)
        
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
        id_viking = random.randrange(len(self.vikingArmy)-1)
        id_saxon = random.randrange(len(self.saxonArmy)-1)

        viking_selected = self.vikingArmy[id_viking]
        saxon_selected = self.saxonArmy[id_saxon]

        result = saxon_selected.receiveDamage(viking_selected.attack())

        if "died in combat" in result:
            self.saxonArmy.pop(id_saxon)
        
        return result

    
    def saxonAttack(self):
        id_viking = random.randrange(len(self.vikingArmy)-1)
        id_saxon = random.randrange(len(self.saxonArmy)-1)

        viking_selected = self.vikingArmy[id_viking]
        saxon_selected = self.saxonArmy[id_saxon]

        result = viking_selected.receiveDamage(saxon_selected.attack())

        if "died in combat" in result:
            self.vikingArmy.pop(id_viking)
        
        return result


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
