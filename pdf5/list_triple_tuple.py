# split a sentence into words and create a
# new list containing, for each word:
# - the word in capitals
# - the word in lowercase
# - the lenght
#
# rewrite the code using a lambda funciton


def tripleTuple(item):
    return str.lower(item), str.upper(item), len(item)


sentence = "Nel mezzo del cammin di nostra vita mi ritrovai in una selva oscura che la diritta via era smarrita"

print(list(map(tripleTuple, sentence.split())))


# Using a lambda function
print(list(map(lambda x: (str.lower(x), str.upper(x), len(x)), sentence.split())))
