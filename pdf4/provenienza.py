# Programma sondaggio sulla provenienza: il programma conterrà un dizionario
# che associa username fittizi a città di provenienza.
# Il programma deve calcolare il numero di utenti per città e stampare la lista in
# ordine decrescente. Inoltre, deve stampare il numero di utenti che non ha
# ancora risposto al sondaggio.

citta_utenti = {
    "mario": "milano",
    "placo": "empoli",
    "franchino": "napoli",
    "darkclaudio": "fighille",
    "freerider": "",
    "osvaldo": "napoli",
    "carlino": "",
}

numero_utenti = {"senza_nome": 0}

for x in citta_utenti.values():
    if x == "":
        numero_utenti["senza_nome"] += 1
    elif x not in numero_utenti:
        numero_utenti[x] = 1
    else:
        numero_utenti[x] += 1

for x in sorted(numero_utenti.items(), key=lambda x: x[1], reverse=True):
    print(x)
