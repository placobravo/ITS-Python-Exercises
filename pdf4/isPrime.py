# Test di primalità su di un numero dato in input.

from math import sqrt


def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if isPrime(int(input("Inserisci un numero: "))):
    print("Il numero inserito è primo.")
else:
    print("Il numero inserito non è primo.")
