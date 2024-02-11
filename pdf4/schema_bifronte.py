# Realizzazione di un programma che data una frase in ingresso, restituisca una nuova frase le cui singole parole siano lo schema bifronte di quelle dell'input
# Es: input: “Mi piace tanto ITS”, output: “iM ecaip otnat STI”

for x in str.split(input("Inserisci una frase: ")):
    print(x[::-1], end=" ")
