# Using the filter function, find the values that are commond to two lists
import random

lista1 = [random.randint(1, 100) for x in range(100)]
lista2 = [random.randint(1, 100) for x in range(100)]


def isIn(x, lista):
    if x in lista:
        return True


print(list(filter(isIn(lista=lista2), lista1)))
