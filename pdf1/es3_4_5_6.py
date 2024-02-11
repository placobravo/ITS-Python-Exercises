# Esercizio 2. Data una stringa x = "testo", aprire il manuale
# del metodo replace delle stringhe.

# Esercizio 3. Creare alcune variabili: a e b di valore intero
# 12 e 23, c e d di valore intero lungo 34 e 45, x e y di
# valore 21.0 e 14.0. Creare un'altra variabile pi di valore 3.141593.
# Di che tipo è?

# Esercizio 4. Usando print, stampare a schermo la variabile a.
# Stampare a e b, sulla stessa riga. Stampare a e b
# sulla stessa riga, separate da un punto e virgola.

# Esercizio 5. Usando print, stampare a schermo il prodotto di a e b.
# Assegnare ad r il risultato del prodotto di a
# e b.

a, b, c, d, x, y, pi = 12, 23, 34, 45, 21.0, 14.0, 3.141593
print(a, b, c, x, y, pi)

print("Il tipo di variabile di pi è: ", type(pi))

print(a, ";", b, sep="")

# You can also do
print(f"{a};{b}")

r = a * b

print(
    a * b,
    c - d,
    x / y,
    a // b,
    c // d,
    x // y,
    a * c,
    b * y,
    2**107,
    2**100,
    2**1.2,
    2**-2,
    4 ** (1 / 2),
)
print(type(a * b))
