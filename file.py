from vikingsClasses import War, Viking, Saxon
import random

def crear_equipo_viking(guerra, nombres):
    for i in nombres:
        guerra.addViking(Viking(i, 100, random.randint(0,100)))

def crear_equipo_saxon(guerra, numero_saxones):
    for i in range(0, numero_saxones):
        guerra.addSaxon(Saxon(50, random.randint(0,100)))

def luchar(guerra):
    ronda = 1
    while guerra.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(guerra.vikingAttack())
        if(guerra.showStatus() == "Vikings and Saxons are still in the thick of battle."):
            print(guerra.saxonAttack())
        print(f"Ronda {ronda}. Estado: {guerra.showStatus()}")
        ronda += 1

vikingos = ["Toni", "Maksym", "Ivan", "Marc"]
saxons = 10

guerra = War()

crear_equipo_viking(guerra, vikingos)
crear_equipo_saxon(guerra, saxons)
luchar(guerra)

