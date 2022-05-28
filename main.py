import pygame
import klase
import sys
import random


print("Welcome to the game!")
print("You are a brave adventurer who has been kidnapped by the evil wizard.")
print("You must find the wizard and save the princess!")
# pick your hero
print("Choose your hero:")
print("1. Swordsman" + "\n" + "2. Wizard")
input_hero = input("Choose your hero: ")
if input_hero == "1":
    hero = klase.Swordsman()
    print("You have chosen Swordsman")
    print("Your health is: " + str(hero.get_health()))
    print("Your backpack is: " + str(hero.get_backpack()))
    print("Your hand is: " + str(hero.get_hand()))
elif input_hero == "2":
    hero = klase.Wizard()
    print("You have chosen Wizard")
    print("Your health is: " + str(hero.get_health()))
    print("Your backpack is: " + str(hero.get_backpack()))
    print("Your hand is: " + str(hero.get_hand()))
else:
    print("You have to choose your hero, yet your choice is not valid.")
    print("You have to type 1 or 2.")

# starter items
sword = klase.Sword()
potion = klase.Potion()
spell = klase.Spell()

#pick up items
hero.pick_up_item(potion)
hero.pick_up_item(spell)
hero.pick_up_item(sword)

#pick your enemy
print("Choose your enemy:")
print("dragon or spider")
input_enemy = input("Choose: ")
if input_enemy == "dragon":
    enemy = klase.Dragon()
    print("You have chosen dragon")
    print("It's health is: " + str(enemy.get_health()))
elif input_enemy == "spider":
    enemy = klase.Spider()
    print("You have chosen spider")
    print("It's health is: " + str(enemy.get_health()))
else:
    print("You have to choose your enemy, yet your choice is not valid.")
    print("You have to type dragon or spider.")

klase.battle(hero, enemy)
    
