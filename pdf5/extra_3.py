# Using the filter function, find the values that are commond to two lists

import random

lista1 = [random.randint(1, 100) for x in range(100)]
lista2 = [random.randint(1, 100) for x in range(100)]


def isIn(lista=lista1):
    def isInLista(x):
        return x in lista

    return isInLista


inLista1 = isIn(lista1)

print(list(filter(inLista1, lista2)))
