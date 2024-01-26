# is prime


def isPrime(number):
    for x in range(2, number):
        if number % x == 0:
            return False

    return True


prova = int(input("Inserisci un numero: "))

if isPrime(prova):
    print("wow")
