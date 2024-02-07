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
