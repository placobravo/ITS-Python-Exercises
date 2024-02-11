# Scrivere un programma che legga il file dell’esercizio
# precedente e generi un dizionario le cui chiavi siano costituite dai
# numeri esadecimali letti e i valori associati alla chiave siano dati
# dalle occorrenze dei numeri stessi.
# Es: se nel file il numero F5 appare 13 volte il dizionario
# sarà così composto D = {…, “F5”: 13, ...}

try:
    with open("hex_casuali.txt", "r") as hex_file:
        hex_list = [x.rstrip() for x in hex_file.readlines()]

except FileNotFoundError as err:
    print(err, "\nYou need to create the text file first!")

else:
    hex_dizionario = {}
    for x in hex_list:
        if x in hex_dizionario:
            hex_dizionario[x] += 1
        else:
            hex_dizionario[x] = 1

    print(hex_dizionario)


# The following code uses the zip method by creating two different lists.
# It's less efficient but it's more fun!
#
#    hex_key = []
#
#    for x in hex_list:
#        if x not in hex_key:
#            hex_key.append(x)
#
#    hex_value = []
#
#    for x in hex_key:
#        hex_value.append(hex_list.count(x))
#
#    hex_dizionario = dict(list(zip(hex_key, hex_value)))
#
#    print(hex_dizionario)
