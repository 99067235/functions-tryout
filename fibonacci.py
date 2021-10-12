def fib(numberOfTerms):
    teller = 0

    a = 0
    b = 1
    c = 0

    while teller <= numberOfTerms:
        print(a)
        c = a + b
        a = b
        b = c
        teller = teller + 1

fib(10)