from random import randint
from colorama import init, Fore, Style
init()

class GameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def attack(self, other, color):
        damage = randint(10, 80)
        print(Style.BRIGHT)

        print(color + "{} attacks {} with power {}".format(self.name, other.name, damage))
        other.life -= damage
        print("{}'s Life: {}; {}'s Life: {}".format(self.name, other.name, self.life, other.life))
        print(Style.RESET_ALL)


class Hero(GameCharacter):
    pass

class Enemy(GameCharacter):
    pass

def check_life(hero, enemy):
    if hero.life <= 0:
        # Game ended
        
        print("The Enemy won!")
        return False
    elif enemy.life <= 0:
        # Game ended
        
        print("The Hero won!")
        return False
    else:
        return True


hero = Hero("Player", 100)
enemy = Enemy("Evil", 100)

input(Fore.CYAN + "Press Enter to Start the Game: ")

# Game Loop
while check_life(hero, enemy):
    rand_num = randint(0, 10)

    if rand_num == 0:
        # Hero attacks Enemy

        hero.attack(enemy, Fore.GREEN)
    elif rand_num == 10:
        # Enemy attacks Hero

        enemy.attack(hero, Fore.RED)
    else:
        print(Fore.YELLOW + "wait...")
    
else:
    print(Fore.MAGENTA + "## THE END ##")
    print()
