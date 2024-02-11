# Trovare gli indici di tutte le occorrenze della variabile val1 nella lista mylist, entrambe inserite in input da
# tastiera. Il risultato, sotto forma di lista, va visualizzato sullo schermo.
# Ad esempio, se val1 = 1 e mylist = [1, 3, 6, 9, 1, 1, 2, 1, 2] il risultato deve essere [0, 4, 5, 7].

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

for i in range(len(lista)):
    if val1 == lista[i]:
        nuovalista.append(i)

print(nuovalista)
