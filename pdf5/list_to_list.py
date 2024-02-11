# Elevate each number of one list to the corresponding number of the other list

import random

lista1 = [random.randint(1, 20) for x in range(7)]
lista2 = [x for x in range(7)]

print(lista1)

for i in range(len(lista1)):
    lista1[i] = lista1[i] ** lista2[i]

print(lista1)
