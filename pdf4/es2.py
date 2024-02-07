# Realizzazione di un programma che data una frase in ingresso, restituisca una nuova frase le cui singoel parole siano lo schema bifronte di quelle dell'input

for x in str.split(input("Inserisci una frase: ")):
    print(x[::-1], end=" ")
