# Dal sito https://it.lipsum.com si scarichino i primi 5 paragrafi di Lorem Ipsum,
# salvandoli su un file di testo chiamato “lorem.txt”. Data una stringa da tastiera
# (parola), si apra il file e si contino le occorrenze della parola nel file,
# stampando a video il risultato.

lorem_text = ""
counter = 0

parola = input("Inserisci una parola da cercare: ")

with open("lorem.txt", "r") as lorem:
    for line in lorem:
        lorem_text += line

for word in lorem_text.split():
    if parola in word:
        counter += 1

print(f""""{parola}" compare {counter} volte.""")
