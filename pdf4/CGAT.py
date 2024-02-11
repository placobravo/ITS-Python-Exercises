# Creare una stringa di 40.000 caratteri scelti a caso dall'alfabeto 'CGAT'.

from random import choice

letters = ["C", "G", "A", "T"]
randword = ""
dna_lenght = 40000

for i in range(dna_lenght):
    randword += choice(letters)

print(randword)
