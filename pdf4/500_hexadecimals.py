# Scrivere un programma che generi 500 numeri casuali tra 0 e 255,
# li converta in esadecimale, con formato a due cifre, e li
# scriva come singole righe in un file di testo denominato “numeri.txt”.

from random import randint

dec_casuali = [randint(0, 255) for x in range(500)]
hex_casuali = [f"{x:0>2X}" for x in dec_casuali]

try:
    hex_file = open("hex_casuali.txt", "x")
except FileExistsError as err:
    print(
        err,
        "\nMake sure to delete your 'hex_casuali.txt' file before using this script!",
    )
else:
    for x in hex_casuali:
        hex_file.writelines(x + "\n")
    print("File has been written, bye!")
