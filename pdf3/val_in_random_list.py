# Trovare gli indici di tutte le occorrenze della variabile val1 nella lista mylist, entrambe inserite in input da
# tastiera. Il risultato, sotto forma di lista, va visualizzato sullo schermo.
# Ad esempio, se val1 = 1 e mylist = [1, 3, 6, 9, 1, 1, 2, 1, 2] il risultato deve essere [0, 4, 5, 7].
# Riprendere l’esercizio n.3 con la seguente variante: mylist è popolata con numeri casuali generati dalla
# funzione randint

import random

lista = [random.randint(1, 100) for x in range(1000)]

val1 = int(input("\nInserisci un numero da cercare nella lista: "))

if val1 in lista:
    print(val1, "è nella lista")

nuovalista = []

for i in range(len(lista)):
    if val1 == lista[i]:
        nuovalista.append(i)

print(nuovalista)
