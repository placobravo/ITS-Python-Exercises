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


def mcm(primes_dictionaries_list):
    dmcm = {}
    mcm = 1

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


def MCD(primes_dictionaries_list):
    dmcd = {}
    mcd = 1

    # Scan all the keys in the first dictionary, and see
    # if a key is in all the other dictionaries
    for key in primes_dictionaries_list[0]:
        for prime_dictionary in primes_dictionaries_list:
            # If key in any dictionary we compare its value
            # and only add it if it's lower
            if key in prime_dictionary:
                if key in dmcd:
                    if dmcd[key] > prime_dictionary[key]:
                        dmcd[key] = prime_dictionary[key]
                else:
                    dmcd[key] = prime_dictionary[key]

            # If key not in any prime_dictionary we break
            # the cycle and remove the key from dmcd
            else:
                dmcd.pop(key)
                break

    # Now simply multiply each dict key to the power
    # of its corresponding value
    for key in dmcd:
        mcd = mcd * (key ** dmcd[key])

    return mcd


############################################################

int_list = []
primes_dictionaries_list = []

try:
    while True:
        int_list.append(int(input("Inserisci un intero: ")))
except KeyboardInterrupt:
    pass

print("\n" * 5)


# Create a list of dictionaries with primes factors
for x in int_list:
    primes_dictionaries_list.append(primeFactors(x))


# If list is empty or one element return 0 or the element itself
if len(int_list) == 1:
    print(int_list[0])
elif len(int_list) == 0:
    print(0)
else:
    print("Il massimo comune divisore è: ", MCD(primes_dictionaries_list))
    print("Il minimo comune multiplo è: ", mcm(primes_dictionaries_list))
