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


def first_last_same(lista):
    counter = 0
    for item in lista:
        if len(item) > 1 and item[0] == item[-1]:
            counter += 1

    return counter


#
# ---------------------------------------------------
#

# The list gets created here
my_list = []
while True:
    n = input(
        "Insert an element for the list, items divided by ';' will be also interpreted as a list: "
    )
    if n == "fine":
        break
    my_list.append(n)


# This creates a new list made with numbers only. Lists of numbers are ignored
my_list_numbers = []
for i in my_list:
    try:
        my_list_numbers.append(float(i))
    except Exception:
        continue

# This creates a list of tuples of numbers with all the strings that are written as *number*;*number* in my_list.
# Each item will become a tuple of numbers in the new my_list_number_tuples
# For example the string "5342.53;8;9.1;-10.5" will become a tuple of numbers, and be an item in my_list_number_tuples as (5342.53, 8, 9.1, -10.5)
my_list_number_tuples = ()
for i in my_list:
    for char in i:
        if not str.isdecimal(char) and char != ";" and char != "." and char != "-":
            break


while True:
    while True:
        print(
            "\nChose an operation to do on your list:\n1- Sum\n2- Product\n3- Greatest number on the list\n4- Smallest number on the list\n5- Number of items with the same first and last character\n6- Stop the program"
        )
        scelta = input("Fai una scelta: ")
        if str.isdecimal(scelta) and int(scelta) >= 1 and int(scelta) <= 6:
            scelta = int(scelta)
            break
        else:
            print("Please make a correct choice!")

    match scelta:
        case 1:
            print("The sum is:", totalSum(my_list_numbers))
        case 2:
            print("The product is:", totalProduct(my_list_numbers))
        case 3:
            print("Greatest number in the list is:", isGreatest(my_list_numbers))
        case 4:
            print("Smallest number in the list is:", isSmallest(my_list_numbers))
        case 5:
            print(
                "Numbers of string with the same first and last characters:",
                first_last_same(my_list),
            )
        case 6:
            print("Bye!")
            break
        case _:
            print("Make a correct choice")

    while True:
        scelta = input("Do you want to make another choice? (Y/n): ")
        if scelta == "y" or scelta == "Y" or scelta == "":
            break
        elif scelta == "n" or scelta == "N":
            break
        else:
            print("Make a correct choice!")

    if scelta == "n" or scelta == "N":
        print("Bye!")
        break


# TODO number 5
# TODO make it so that my_list_numbers also includes numbers from lists
