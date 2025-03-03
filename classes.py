from random import randint

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        # Random damage function 
        damage = randint(1, self.attack_power)

        if damage == 5 or damage == 25:
            damage *= 2
            print(f"CRITICAL HIT! ", end="")
 
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

        if not hasattr(opponent, 'evadeNextAttack'):
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage! ")
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == False:
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == True:
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack == False  

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# Create Elf class
class Elf(Character):
    def __init(self, name):
        super().__init__(name, health=100, attack_power=20)
    def special_ability(self, opponent):
        print('\n Select special ability')
        print('1. Damage reduction')
        print('2. Avoid damage')

        action = ("Choose an ability: ")

# Create Rogue

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.evadeNextAttack = False 

    def special_ability(self, opponent):
        print('\n Select special ability ')
        print('1. Attack Boost ')
        print('2. Siphoning Strike ')
        print('3. Preemtive Dodge')

        action = input("Choose an ability: ")

        if action == '1':
            self.attack_power += 20
            print(f"{self.name} just increased their attack power to {self.attack_power} ")
        elif action == '2':
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} uses Health Siphon and takes away {self.attack_power} health from {opponent.name} and regenerated health to {self.health}. ")
        elif action == '3':
            self.evadeNextAttack == True
            print(f"{self.name} Uses Preemtive Dodge and will evade the next attack!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
