from dice import d6
from dataclasses import dataclass
from random import choice

@dataclass
class Creature:
    name : str
    hit_point : int
    max_hp : int

    def heal(self, amount):
        self.hit_point = min(self.hit_point + amount, self.max_hp) #ei kasva max_hpta isommaksi -> min palauttaa aina arvoista pienimmän
    
    def damage(self, amount):
        self.hit_point -= amount
    
    def __str__(self):
        return f"Creature ({self.name}, {self.hit_point})"


@dataclass
class MagicUser(Creature):
    energy : int 
    def cure_wounds(self):
        amount = d6()+1
        self.heal(amount)
        self.energy -= 1
        return amount

    def magic_attack(self, target):
         amount = d6()+1
         target.damage(amount)
         self.energy -= 1
         return amount

rounds = 10
wizard_count = 3
red_wizard = MagicUser("Red Wizard", 10, 10, 6)
blue_wizard = MagicUser("Blue Wizard", 12, 12, 4)
yellow_wizard = MagicUser("Yellow Wizard", 8, 8, 8)
wizards = [red_wizard, blue_wizard, yellow_wizard]

for i in range(1, rounds):
    print("ROUND: ", 1)
    for wizard in wizards:
        if wizard.hit_point > 0 and wizard.energy > 0:
            if wizard.hit_point < wizard.max_hp-2 and d6() < 4:
                amount = wizard.cure_wounds()
                print(f"{wizard.name} heals {amount} hp")
            else:
                targets = wizards[:] #kopio wizards listasta
                targets.remove(wizard) #poista itsensä
                if targets:
                    target = choice(targets)
                    amount = wizard.magic_attack(target)
                    print(f"{wizard.name} attacks {target.name} doing {amount} damage")
                    if target.hit_point <= 0:
                        print(target.name, " died!")
                        wizards.remove(target)
        print(wizard)
    
    total_energy = 0
    for wizard in wizards:
        total_energy += wizard.energy
    if total_energy == 0:
        print("Wizard ran out of energy. Draw!")
        break
    if len(wizards) <= 1: #Jos ainoastaan yksi velho jäljellä listassa
        print(f"{wizards[0].name} won!")
        break





