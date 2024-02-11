# Realizzazione di una funzione che ricevuto in ingresso una tupla di numeri interi ne
# calcoli lo MCD e lo restituisca
#
# Realizzazione di una funzione che ricevuto in ingresso una tupla di numeri interi ne
# calcoli lo mcm e lo restituisca
#
# Realizzazione di una funzione che ricevuto in ingresso un numero intero restituisca
# una tupla contenente i suoi divisori
from functools import reduce
from random import randint


# Massimo Comune Divisore di due numeri con teorema di euclicde
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Minimo comune multiplo di due numeri (a partire dal massimo comune divisore)
def mcm(a, b):
    return a * b // mcd(a, b)


# Per calcolare l'mcd o l'mcm di più numeri basta iterare il calcolo tra
# la lista di numeri
def mcm_mcd(func):
    def iteration(int_list):
        return reduce(func, int_list)

    return iteration


mcd_calcolatore = mcm_mcd(mcd)
mcm_calcolatore = mcm_mcd(mcm)

randomlist = [randint(1, 1000) for x in range(10)]

print(randomlist)
print(f"Il massimo comune divisore è: {mcd_calcolatore(randomlist)}")
print(f"Il minimo comune multiplo è: {mcm_calcolatore(randomlist)}")
