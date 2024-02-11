# Si generi un dizionario che abbia come chiave i primi 50 numeri e per
# elemento una tupla dei suoi divisori. Si stampi a video il dizionario.
# Successivamente di memorizzi il dizionario in un file chiamato “divisori.txt”

# Create a generator the gives us the divisors.
# As a last iteration it will give the integer itself
def findDivisors(integer):
    for x in range(1, integer // 2 + 1):
        if integer % x == 0:
            yield x
    yield integer


dictionary = {
    x: y
    for (x, y) in zip(
        [a for a in range(51)], [tuple(z for z in findDivisors(b)) for b in range(51)]
    )
}

print(dictionary)

with open("divisori.txt", "x") as divisori_file:
    for key in dictionary:
        divisori_file.write(str(key))
        divisori_file.write(" : ")
        divisori_file.write(str(dictionary[key]))
        divisori_file.write("\n")
