# Using the filter function, find the values that are commond to two lists
import random

lista1 = [random.randint(100) for x in range(100)]
lista2 = [random.randint(100) for x in range(100)]


def isEqual(x, y):
    if x == y:
        return x


print(list(map(isEqual(lista2, lista1))))
