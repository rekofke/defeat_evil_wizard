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

# Warrior class
#     
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def special_ability(self, opponent):
        print('\nSelect special ability:')
        print('1. Sunder Strike')
        print('2. Shield of fury')
        action = input("Choose an ability: ")
        
        if action == '1':
            damage = int(1.5 * self.attack_power)
            opponent.health -= damage
            print(f"\n{self.name} uses Sunder Strike, slamming {opponent.name} for {damage} damage!")

            opponent.regen_blocked = True

            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")

        if action == '2':
            opponent.attack_power == opponent.attack_power // 2
            print(f"{self.name} uses Shield of fury and blocks half of the damage dealt.")
    
        


# Mage class 
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# Elf class
class Elf(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
    def special_ability(self, opponent):
        print('\n Select special ability')
        print('1. Attack Boost ')
        print('2. Magic Heal')
        

        action = input("Choose an ability: ")

        if action == '1':
            self.attack_power += 20
            print(f"{self.name} used Attack Boost and increased their attack power to {self.attack_power}. ")
        elif action == '2':
            self.health == (self.health + self.max_health // 2)
            print(f"]\n{self.name} uses Magic Heal to boost their health to {self.max_health}. ")


# Rogue Clas

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.evadeNextAttack = False 

    def special_ability(self, opponent):
        print('\n Select special ability ')
        print('1. Siphoning Strike ')
        print('2. Preemtive Dodge')

        action = input("Choose an ability: ")
        
        if action == '1':
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} uses Health Siphon and takes away {self.attack_power} health from {opponent.name} and regenerated health to {self.health}. ")
        elif action == '2':
            self.evadeNextAttack == True
            print(f"{self.name} Uses Preemtive Dodge and will evade the next attack!")

# EvilWizard class 
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.regen_blocked = False

    def regenerate(self):
        if self.regen_blocked:
            print(f"{self.name}'s regeneration was suppressed!")
            self.regen_blocked = False  
            return
        
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

