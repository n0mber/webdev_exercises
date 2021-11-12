from random import *

def die(n=1, sides=6):
    total = 0
    for i in range(n):
        total += randint(1, sides)
    return total



def d6(n=1):
    return die(n, 6)

