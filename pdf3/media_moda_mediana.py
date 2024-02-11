# Data una lista generata attraverso la funzione randint, se ne stampi la media aritmetica, la moda e la mediana.

from random import randint

lista = [randint(1, 1000) for x in range(100)]

print("La lista è:\n", lista)


def listaMedia(x):
    return sum(x) / len(x)


def listaMediana(x):
    x.sort()
    if not len(x) % 2:
        return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
    else:
        return x[len(x) // 2]


def listaModa(x):
    moda = x[0]
    for i in x:
        if x.count(i) > moda:
            moda = x.count(i)
    return moda if x.count(moda) > 1 else "Non c'è moda"


print("\n")
print("La media è: ", listaMedia(lista))
print("La moda è : ", listaModa(lista))
print("la mediana è: ", listaMediana(lista))
