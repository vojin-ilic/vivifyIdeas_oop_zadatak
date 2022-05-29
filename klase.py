
import random
from turtle import position

#random item picker from the ground
def rand_item_from_ground():
    random_number = random.randint(0,len(ground)-1)
    return ground[random_number]

# battle function
def battle(hero, monster):
    while hero.get_health() > 0 and monster.get_health() > 0:
        random_number = random.randint(0,100)
        if random_number < 50:
            hero.pick_up_item(rand_item_from_ground())
            #hand is not empty
            print("You picked up an item: " + str(hero.get_hand()) + " and your hand is now: " + str(hero.get_hand()))
            hero.attack(monster)
            print("Hero attacks monster")
            print("Monster health: " + str(monster.get_health()))
            print("Hero health: " + str(hero.get_health()))
        else:
            monster.attack(hero)
            print("Monster attacks hero")
            print("Monster health: " + str(monster.get_health()))
            print("Hero health: " + str(hero.get_health()))
    if hero.get_health() <= 0:
        print("You have been killed by the monster.")
        #log to file
        with open("log.txt", "a") as log:
            log.write("You have been killed by the monster.")
    elif monster.get_health() <= 0:
        print("You have killed the monster.")
        #log to file
        with open("log.txt", "a") as log:
            log.write("You have killed the monster.")


global ground
ground = []


def get_ground():
    return ground


def drop_item(item):
    ground.append(item)

# hero class
class Hero:
    def __init__(self, backpack=[], health=0, hand=[]):
        self.backpack = backpack
        self.health = health
        self.hand = hand

    def add_to_backpack(self, item):
        try:
            if len(self.backpack) < 3:
                self.backpack.append(item)
        except:
            print("Backpack is full")            

    def remove_from_backpack_to_hand(self, item):
        self.add_to_hand(item)
        self.backpack.remove(item)

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_backpack(self):
        return self.backpack

    def get_hand(self):
        return self.hand

    def set_hand(self, hand):
        self.hand = hand

    def add_to_hand(self, item):
        if self.get_hand() == []:
            self.set_hand([item])
        else:
            print("You can't hold more than one item in your hand")

    def attack(self, monster):
        if type(self.hand) == Sword:
            monster.set_health(monster.get_health() - 10)
            # log to file
            print("You hit the monster with your sword")
            with open("log.txt", "a") as log:
                log.write("You hit the monster with your sword\n")
                log.write("you dropped your sword\n")
            # drop wepon on the ground
            self.remove_from_hand(self.hand)
        elif type(self.hand) == "Spear":
            monster.set_health(monster.get_health() - 15)
            # log to file
            print("You hit the monster with your spear")
            with open("log.txt", "a") as log:
                log.write("You hit the monster with your spear\n")
                log.write("you dropped your spear\n")
            # drop wepon on the ground
            ground.append(self.hand)
            self.remove_from_hand(self.hand)
        elif type(self.hand) == "Spell":
            monster.set_health(monster.get_health() - 20)
            # log to file
            print("You hit the monster with your spell")
            with open("log.txt", "a") as log:
                log.write("You hit the monster with your spell\n")
                log.write("you dropped your spell\n")
            # drop wepon on the ground
            self.remove_from_hand(self.hand)
        elif self.hand == type(Potion):
            self.heal(self.hand)
        else:
            print("You can't hit the monster with your hand")
            with open("log.txt", "a") as log:
                log.write("You can't hit the monster with your hand\n")
                log.write("Monster health: " + str(monster.get_health()) + "\n")
                log.write("Your health: " + str(self.get_health()) + "\n")
                log.write("\n")
        if monster.get_health() <= 0:
            print("You killed the monster!")
            with open("log.txt", "a") as log:
                log.write("You killed the monster!\n")
                log.write("Monster health: " + str(monster.get_health()) + "\n")
                log.write("Your health: " + str(self.get_health()) + "\n")
                log.write("\n")
                

    def remove_from_hand(self, item):
        self.hand = []
        ground.append(item)
        item.set_position("on_ground")

    def heal(self, item):
        if item == type(Potion):
            self.set_health(self.get_health() + 20)
            print("You healed yourself")
            with open("log.txt", "a") as log:
                log.write("You healed yourself\n")
                log.write("you consumed your potion\n")
            self.remove_from_hand(item)
            #delete potion from ground
            ground.remove(item)

    def pick_up_item(self, item):
        if len(self.backpack) < 2:
            self.add_to_backpack(item)
            self.remove_from_ground(item)
            print("You picked up the item")
            with open("log.txt", "a") as log:
                log.write("You picked up the item\n")
        else:
            print("You can't carry more than 2 items")
            with open("log.txt", "a") as log:
                log.write("You can't carry more than 2 items\n")

    def remove_from_ground(self, item):
        ground.remove(item)


# item class
class Item:
    def __init__(self, position="on_ground"):
        self.position = position
        ground.append(self)
    #set position of item
    def set_position(self, position):
        self.position = position    



# wizard class
class Wizard(Hero):
    def __init__(self, backpack=[], health=150):
        super().__init__(backpack, health)

    def cast_spell(self, spell):
        print("You cast " + spell)

    # only allow pickup spell
    def pick_up_item(self, item):
        if item.position == "on_ground" and type(item) == Spell:
            self.hand = item
            item.position = "in_hand"
        else:
            print("You can't pick up this item")


# swordsman class
class Swordsman(Hero):
    def __init__(self, backpack=[], health=100):
        super().__init__(backpack, health)

    def swing_sword(self):
        print("You swing your sword")

    # disallow picking up spell
    def pick_up_item(self, item):
        if item.position == "on_ground" and type(item) != Spell:
            self.hand = item
            item.position = "in_hand"
        else:
            print("You can't pick up this item")


# potion class
class Potion(Item):
    def __init__(self, position="on_ground"):
        self.position = position
    #string representation of potion
    def __str__(self):
        return "Potion"



# sword class
class Sword(Item):
    def __init__(self, position="on_ground"):
        super().__init__(position)
    #string representation of sword
    def __str__(self):
        return "Sword"


# spell class
class Spell(Item):
    def __init__(self, position="on_ground"):
        super().__init__(position)
    #string representation of spell
    def __str__(self):
        return "Spell"


# spear class
class Spear(Item):
    def __init__(self, position="on_ground"):
        super().__init__(position)
    #string representation of spear
    def __str__(self):
        return "Spear"

# monster class
class Monster:
    def __init__(self, health=100):
        self.health = health

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def hit(self, hero):
        hero.set_health(hero.get_health() - 5)


# spider class
class Spider(Monster):
    def __init__(self, health=50):
        super().__init__(health)

    def bite(self, hero):
        hero.set_health(hero.get_health() - 8)

    def attack(self, hero):
        randi = random.choice(["bite", "hit"])
        if randi == "bite":
            self.bite(hero)
        else:
            self.hit(hero)
        print("You are attacked by a spider")
        print("The spider uses" + randi)
        print("Your health: " + str(hero.get_health()))
        # log to file
        with open("log.txt", "a") as log:
            log.write("You are attacked by a spider\n")
            log.write("The spider uses " + randi + "\n")
            log.write("Your health: " + str(hero.get_health()) + "\n")
            log.write("The spider health: " + str(self.get_health()) + "\n")
            log.write("\n")

# dragon class
class Dragon(Monster):
    def __init__(self, health=200):
        super().__init__(health)

    def breath_fire(self, hero):
        hero.set_health(hero.get_health() - 20)

    def attack(self, hero):
        randi = random.choice(["breath_fire", "hit"])
        if randi == "breath_fire":
            self.breath_fire(hero)
        else:
            self.hit(hero)
        print ("You are attacked by the dragon")
        print ("The dragon uses " + randi)
        print ("You have " + str(hero.get_health()) + " health left")
        #log to file
        with open("log.txt", "a") as log:
            log.write("You are attacked by the dragon\n")
            log.write("The dragon uses " + randi + "\n")
            log.write("You have " + str(hero.get_health()) + " health left\n")
            log.write("\n")
