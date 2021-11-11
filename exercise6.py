from dice import d6
from dataclasses import dataclass

@dataclass
class Creature:
    name : str
    hit_point : int
    max_hit_points : int

    def heal(self, name, hit_point, max_hit_points):
        heal = lambda x : dice.d6() + 1 if hit_point != max_hit_points else max_hit_points
        hit_point = heal
        return hit_points
    
    def damage(self, name, hit_point)
        hit_point -= dice.d6() + 1
        return hit_point


@dataclass
class MagicUser(Creature):
    energy : int 

    #TODO kutsu heal ja damage funktioita - palauta hit_point arvo ja vähennä energy arvo yhdellä
    def cure_wounds(self, name, energy):
        heal()
        return hit_point

    def magic_attack(self, name, hit_point:)
         hit_point -= dice.d6() + 1
         return 

rounds = 10
wizard_count = 3
red_wizard = MagicUser("Red Wizard", hit_point=10, max_hit_point=10, energy=6)
blue = MagicUser("Blue Wizard", hit_point=12, max_hit_point=12, energy=4)
yellow_wizard = MagicUser("Yellow Wizard", hit_point=8, max_hit_point=8, energy=8)

for i in range(1, rounds, 1):
    print(i)



