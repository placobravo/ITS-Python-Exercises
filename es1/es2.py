print("inserisci una stringa")
stringa = input()

charList = {}

for n in stringa:
    if n in charList:
        charList[n] += 1
    else:
        charList[n] = 1


print(charList)
