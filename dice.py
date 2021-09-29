from random import *

def die(n=1, sides=6):
    total = 0
    for i in range(n):
        sides = randrange(1, 6)
        total += sides
    return total



def d6(n=1):
    return randrange(1, 6)

print(die())