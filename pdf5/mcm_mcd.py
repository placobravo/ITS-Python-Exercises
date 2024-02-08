# Realizzazione di una funzione che ricevuto in ingresso una tupla di numeri interi ne
# calcoli lo MCD (Massimo Comune Denominatore) e lo restituisca
#
# Realizzazione di una funzione che ricevuto in ingresso una tupla di numeri interi ne
# calcoli lo mcm (minimo comune multplo) e lo restituisca
from math import sqrt


def primeFactors(int_number):
    prime_factors = {}

    while int_number > 1:
        # The +2 is needed so that we don't end with an infinite loop:
        # sqrt(2) = 1 thus we would get no iteration because range(2,1) is []
        for x in range(2, int(sqrt(int_number) + 2)):
            if int_number % x == 0:
                if x in prime_factors:
                    prime_factors[x] += 1
                else:
                    prime_factors[x] = 1
                int_number = int_number // x
                break
        else:
            if int_number in prime_factors:
                prime_factors[int_number] += 1
            else:
                prime_factors[int_number] = 1
            int_number = 0

    return prime_factors


def mcm(int_list):
    primes_dictionaries_list = []
    dmcm = {}
    mcm = 1

    if len(int_list) == 1:
        return int_list[0]
    elif len(int_list) == 0:
        return 0

    # Create a list of dictionaries with primes factors
    for x in int_list:
        primes_dictionaries_list.append(primeFactors(x))

    # Scan each dictionary in list and find each unique
    # largest prime factor amongst all the dictionaries
    for primes_dict in primes_dictionaries_list:
        for key in primes_dict:
            if key in dmcm:
                if dmcm[key] < primes_dict[key]:
                    dmcm[key] = primes_dict[key]
            else:
                dmcm[key] = primes_dict[key]

    # Now simply multiply each dict key to the power
    # of its corresponding value
    for key in dmcm:
        mcm = mcm * (key ** dmcm[key])

    return mcm


def MCD(int_list):
    primes_dictionaries_list = []
    mcd = 1
    dmcd = {}

    if len(int_list) == 1:
        return int_list[0]
    elif len(int_list) == 0:
        return 0

    # Create a list of dictionaries with primes factors
    for x in int_list:
        primes_dictionaries_list.append(primeFactors(x))

    # Scan each dictionary in list and find each unique
    # largest prime factor amongst all the dictionaries
    for key in primes_dictionaries_list[0]:
        for prime_dictionary in primes_dictionaries_list:
            if key in prime_dictionary:
                continue
            else:
                break
        else:
            if key in dmcd:
                if dmcd[key] < primes_dictionaries_list[0][key]:
                    dmcd[key] = primes_dictionaries_list[0][key]
            else:
                dmcd[key] = primes_dictionaries_list[0][key]

    # Now simply multiply each dict key to the power
    # of its corresponding value
    for key in dmcd:
        mcd = mcd * (key ** dmcd[key])

    return mcd


############################################################

int_list = []

try:
    while True:
        int_list.append(int(input("Inserisci un intero: ")))
except KeyboardInterrupt:
    pass

print("\n" * 5)

print(MCD(int_list))
