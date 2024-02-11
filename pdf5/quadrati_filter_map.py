# Utilizzare la list comprehension per creare la lista dei primi dieci quadrati:
# a = [0, 1, 4, 9…]; si creino, successivamente, due nuove funzioni che accettino in
# input la lista precedente e restituiscano in output due tuple, secondo le seguenti
# specifiche:
# - solo numeri pari, utilizzando internamente la funzione filter
# - la radice quadrata, utilizzando internamente la funzione map lista coi primi 10 quadrati

from math import sqrt


def isEven(x):
    return x % 2 == 0


def onlyEven(lista):
    return tuple(filter(isEven, lista))


def squaredElements(lista):
    return tuple(map(sqrt, lista))


# -------------------------------------------------


quadrati = [x**2 for x in range(11)]


print(quadrati)
print(onlyEven(quadrati))
print(squaredElements(quadrati))
