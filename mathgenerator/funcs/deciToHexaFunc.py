from .__init__ import *


def deciToHexaFunc(max_dec=1000):
    a = random.randint(0, max_dec)
    b = hex(a)
    problem = "Binary of " + str(a) + "="
    solution = str(b) 

    return problem, solution
