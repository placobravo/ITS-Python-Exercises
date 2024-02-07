from random import choice

letters = ["C", "G", "A", "T"]
randword = ""
dna_lenght = 40000

for i in range(dna_lenght):
    randword += choice(letters)

print(randword)
