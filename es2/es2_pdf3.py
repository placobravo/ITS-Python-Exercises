lista = []
max_tentativi = 5
tentativi = 1

while (tentativi <= max_tentativi):
    n = int(input("Inserisci un numero: "))
    if n not in lista:
        lista.append(n)
        tentativi += 1

print(lista)
