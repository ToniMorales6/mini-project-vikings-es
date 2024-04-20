
from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]

guerra =  War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        guerra.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))


#Create 5 Saxons
for i in range(0,5):
    if i:
        guerra.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while guerra.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    guerra.vikingAttack()
    guerra.saxonAttack()
    print(f"round: {round} // Viking army: {len(guerra.vikingArmy)} warriors",f"and Saxon army: {len(guerra.saxonArmy)} warriors")
    print(guerra.showStatus())
    round += 1