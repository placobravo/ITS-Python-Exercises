# Scrivere un programma che, presa una lista di nomi di file, mostri il contenuto
# di ognuno dei file.
# Gestire l’eventuale mancanza di alcuni dei file nel disco.

nomi_files = ["animali.txt", "automobili.txt", "cose.txt", "città.txt"]

for x in nomi_files:
    try:
        with open(x, "r") as temp:
            print(temp.read())
    except FileNotFoundError as e:
        print(e)
