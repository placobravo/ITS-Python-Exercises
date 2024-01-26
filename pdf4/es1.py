cubi = [x**3 for x in list(range(11))]
even = ()
times3 = ()

for i in cubi:
    if i % 2 == 0:
        even = even + (i,)

for i in cubi:
    times3 = times3 + (i * 3,)

print(cubi)
print(even)
print(times3)
