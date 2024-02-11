# Utilizzare la list comprehension per creare la lista dei primi dieci cubi:
# a = [0, 1, 8, 27…]; si creino, successivamente, due
# nuove tuple derivate dalla precedente che contengano:
# - solo numeri pari
# - gli elementi della lista di partenza moltiplicati per 3

cubi = [x**3 for x in range(11)]
even = set(i for i in cubi if i % 2 == 0)
times3 = set(i * 3 for i in cubi)

print(cubi, even, times3, sep="\n")
