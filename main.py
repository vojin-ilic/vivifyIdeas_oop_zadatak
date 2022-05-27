import klase
import sys
import random

#simulate battle betwene hero and monster
def battle(hero, monster):
    with open("battles.txt", "a") as f:
        while hero.get_health() > 0 and monster.get_health() > 0:
            if random.randrange(0, 100) <= 0:
                hero.hit(monster)
                f.write("Hero hits monster with {Hero.hand}\n")
            else:
                monster.hit(hero)
                f.write("Monster hits hero with {Monster.attack}\n") 
        if hero.get_health() > 0:
            print("You win!")
        else:
            print("You lose!")

