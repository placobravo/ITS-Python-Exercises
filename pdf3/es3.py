# Trovare gli indici di tutte le occorrenze della variabile val1 nella lista mylist, entrambe inserite in input da tastiera. Il risultato, sotto forma di lista, va visualizzato a schermo

lista = []

while True:
    try:
        lista.append(input("Inserisci un valore: "))
    except KeyboardInterrupt:
        break

val1 = input("\nInserisci una stringa di testo da cercare nella lista: ")

if val1 in lista:
    print(val1, "è nella lista")

nuovalista = []

for i in range(lista):
    if i in lista[i]:
        lista[i].
