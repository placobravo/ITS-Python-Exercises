# Si scriva un programma che legga 5 numeri interi da tastiera. Il numero letto viene inserito in una lista se e
# soltanto se esso non è una copia di un numero già presente nella lista stessa. Il processo continua finché 5
# numeri diversi tra loro sono inseriti da tastiera.
# A quel punto il programma calcola e stampa il valore medio dei 5 numeri inseriti.

lista = []
max_tentativi = 5
tentativi = 1

while tentativi <= max_tentativi:
    n = int(input("Inserisci un numero: "))
    if n not in lista:
        lista.append(n)
        tentativi += 1

print(lista)

print(sum(lista) / (len(lista)))
