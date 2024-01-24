def totalSum(lista):
    somma = 0
    for i in lista:
        somma += i

    return somma

def totalProduct(lista):
    product = 1
    for i in lista:
        product *= i

    return product

def isGreatest(lista):
    greatest = lista[0]
    for i in lista:
        if i > greatest:
            greatest = i

    return greatest

def isSmallest(lista):
    smallest = lista[0]
    for i in lista:
        if i < smallest:
            smallest = i

    return smallest

#
# ---------------------------------------------------
#

my_list = []

while True:
    n = input("Insert an element for the list: ")
    if n == "fine":
        break
    my_list.append(n)

my_list_numbers = []

for i in my_list:
    try:
        my_list_numbers.append(float(i))
    except:
        continue

while True:

    while True:
        print("\nChose an operation to do on your list:\n1- Sum\n2- Product\n3- Greatest number on the list\n4- Smallest number on the list\n5- Stop the program")
        scelta = input("Fai una scelta: ")
        if (str.isdecimal(scelta) and int(scelta) >= 1 and int(scelta) <= 5):
            scelta = int(scelta)
            break
        else:
            print("Please make a correct choice!")

    match scelta:
        case 1:
            print("The sum is:",totalSum(my_list_numbers))
        case 2:
            print("The product is:",totalProduct(my_list_numbers))
        case 3:
            print("Greatest number in the list is:",isGreatest(my_list_numbers))
        case 4:
            print("Smallest number in the list is:",isSmallest(my_list_numbers))
        case 5:
            print("Bye!")
            break
        case _:
            print("Make a correct choice")

    while True:
        scelta = input("Do you want to make another choice? (Y/n): ")
        if scelta == 'y' or scelta == 'Y' or scelta == "":
            break
        elif scelta == 'n' or scelta == 'N':
            break
        else:
            print("Make a correct choice!")

    if scelta == 'n' or scelta == 'N':
        print("Bye!")
        break


# TODO number 5





