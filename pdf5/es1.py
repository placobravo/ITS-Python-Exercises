# lista coi primi 10 quadrati
#
# fun1 = prendi lista come input e da in output una tupla
#   solo numeri pari con funzione filter
# fun2 = prendi lista come input e da in output una tupla
#   radice quadratra usantdo funzione map
#
from math import sqrt


def isEven(x):
    if x % 2 == 0:
        return True
    return False


def onlyEven(lista):
    return tuple(filter(isEven, lista))


def squaredElements(lista):
    return tuple(map(sqrt, lista))


# -------------------------------------------------


quadrati = [x**2 for x in range(11)]


print(quadrati)
print(onlyEven(quadrati))
print(squaredElements(quadrati))
