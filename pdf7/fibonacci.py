# F(0)=0
# F(1)=1
# F(n) = F(n-1)+F(n-2)


def fibonacciGen(n):
    a, b = 1, 0
    for _ in range(n):
        yield a + b
        a = a + b
        b = a - b


for x in fibonacciGen(
    int(input("How many Fibonacci's number do you want to calculate?: "))
):
    print(x)


# start
#       a = 1
#       b = 0
#
# step 0
#       yield a + b = 1 + 0 = 1
#       a = 1 + 0 = 1
#       b = 1 - 0 = 1
#
# step 1
#       yield a + b = 1 + 1 = 2
#       a = 1 + 1 = 2
#       b = 2 - 1 = 1
#
# step 2
#       yield a +b = 2 + 1 = 3
#       a = 2 + 1 = 3
#       b = 3 - 1 = 2
#
# step 3
#       yield a + b = 3 + 2 = 5
#       a = 3 + 2 = 5
#       b = 5 - 2 = 3
#
# step 4
#       yield a + b = 5 + 3 = 8
#       a = 5 + 3 = 8
#       b = 8 - 3 = 5
#
# etc...
