from bases import Bases
from calculator.evaluation import evaluate
bases = Bases()

def conv_1(i,bs_1, bs_2, bs_3 : str) -> int:
    if i >= 5:
        bs_1 = input(("Enter 1st value").lower)
        bs_2 = input(("Enter 2nd value").lower)
    if i == 6:
        x = bases.fromBase2(bs_1)
        y = bases.fromBase2(bs_2)
        bs_3 = bases.toBase2(evaluate(x, y, z))
    elif i == 7:
        x = bases.fromBase8(bs_1)
        y = bases.fromBase8(bs_2)
        bs_3 = bases.toBase8(evaluate(x, y, z))
    elif  i == 8:
        x = bases.fromBase16(bs_1)
        y = bases.fromBase16(bs_2)
        bs_3 = bases.toBase16(evaluate(x, y, z))
        
    return x,y,bs_3