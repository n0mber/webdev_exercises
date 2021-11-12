from dice import d6
from dataclasses import dataclass

@dataclass
class Creature:
    name : str
    hit_point : int
    max_hp : int

    def heal(self, amount):
        hit_point = min(hit_point + amount, max_hp) #ei kasva max_hpta isommaksi -> min palauttaa aina arvoista pienimmän
    
    def damage(self, amount)
        hit_point -= amount
    
    def __str__(self):
        return f"Creature ({name}, {hit_point})"


@dataclass
class MagicUser(Creature):
    energy : int 
    def cure_wounds(self):
        amount = d6()+1
        self.heal(amount)
        energy -= 1
        return amount

    def magic_attack(self, target):
         amount = d6()+1
         target.damage(amount)
         energy -= 1
         return amount

rounds = 10
wizard_count = 3
red_wizard = MagicUser("Red Wizard", hit_point=10, max_hp=10, energy=6)
blue = MagicUser("Blue Wizard", hit_point=12, max_hp=12, energy=4)
yellow_wizard = MagicUser("Yellow Wizard", hit_point=8, max_hp=8, energy=8)
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
                    if target.hp <= 0:
                        print(target.name, " died!")
                        wizards.remove(target)
        print(wizard)

#TODO katso video 28.1.2021 1:16:36 ->




