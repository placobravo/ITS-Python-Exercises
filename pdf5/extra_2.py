tripleTuple = lambda x: (str.lower(x), str.upper(x), len(x))

sentence = "Nel mezzo del cammin di nostra vita mi ritrovai in una selva oscura che la diritta via era smarrita"

print(list(map(tripleTuple, sentence.split())))
