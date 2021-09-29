from dice import d6
from dataclasses import dataclass

@dataclass
class Creature:
    name : str
    hit_point : int
    max_hit_points : int

    def cure_wounds(self, name, hit_point, max_hit_points):
        heal = lambda x : dice.d6() + 1 if hit_point != max_hit_points else max_hit_points
        return hit_point = heal

    def magic_attack(self, name, hit_point:)
         return hit_point -= dice.d6() + 1