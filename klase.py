#hero class
import random
ground = []

class Hero:
    def __init__(self, backpack = [], health = 0, hand =[]):
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
    def hit(self, monster):
        if self.hand == type(Sword):
            monster.set_health(monster.get_health() - 10)
            #drop wepon on the ground
            ground.append(self.hand) 
            self.remove_from_hand(self.hand)
        elif self.hand == type(Spear):
            monster.set_health(monster.get_health() - 15)
        elif self.hand == type(Spell):
            monster.set_health(monster.get_health() - 20)
    
#item class
class Item:
    def __init__(self, position = "on_ground"):
        self.position = position

#wizard class
class Wizard(Hero):
    def __init__(self, backpack = [], health = 150):
        super().__init__(backpack, health)
    def cast_spell(self, spell):
        print("You cast " + spell)
    #only allow pickup spell
    def pick_up_item(self, item):
        if item.position == "on_ground" and type(item) == Spell:
            self.hand = item
            item.position = "in_hand"
        else:
            print("You can't pick up this item")

#swordsman class
class Swordsman(Hero):
    def __init__(self, backpack = [], health = 100):
        super().__init__(backpack, health)
    def swing_sword(self):
        print("You swing your sword")
    #disallow picking up spell
    def pick_up_item(self, item):
        if item.position == "on_ground" and type(item) != Spell:
            self.hand = item
            item.position = "in_hand"
        else:
            print("You can't pick up this item")

#sword class
class Sword(Item):
    def __init__(self, position = "on_ground"):
        super().__init__(position)

#spell class
class Spell(Item):
    def __init__(self, position = "on_ground"):
        super().__init__(position)

#spear class
class Spear(Item):
    def __init__(self, position = "on_ground"):
        super().__init__(position)

#monster class
class Monster:
    def __init__(self, health = 100):
        self.health = health
    def get_health(self):
        return self.health
    def set_health(self, health):
        self.health = health
    def hit(self, hero):
        hero.set_health(hero.get_health() - 5)

#spider class
class Spider(Monster):
    def __init__(self, health = 50):
        super().__init__(health)
    def bite(self, hero):
        hero.set_health(hero.get_health() - 8)
    def attack(self, hero):
        if random.choice(["bite", "hit"]) == "bite":
            self.bite(hero)
        else:
            self.hit(hero)
#dragon class
class Dragon(Monster):
    def __init__(self, health = 200):
        super().__init__(health)
    def breath_fire(self, hero):
        hero.set_health(hero.get_health() - 20)
    def attack(self, hero):
        if random.choice(["breath_fire", "hit"]) == "breath_fire":
            self.breath_fire(hero)
        else:
            self.hit(hero)