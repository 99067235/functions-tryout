def berekening():
    
    addition(10,12)
    subtraction(58,34)
    multiplication(6,7)
    division(144,12)
    increment(12)
    decrement(34)

def addition(nummer1 = 0, nummer2 = 0):
    antwoord = int(nummer1) + int(nummer2)
    print(nummer1, "+", nummer2,"=", antwoord)

def subtraction(nummer1 = 0, nummer2 = 0):
    antwoord = int(nummer1) - int(nummer2)
    print(nummer1, "-", nummer2, "=", antwoord)

def multiplication(nummer1 = 0, nummer2 = 0):
    antwoord = int(nummer1) * int(nummer2)
    print(nummer1, "*", nummer2, "=", antwoord)

def division(nummer1 = 0, nummer2 = 0):
    antwoord = int(nummer1) / int(nummer2)
    print(nummer1, "/", nummer2, "=", antwoord)

def increment(nummer = 0):
    print(nummer, "+ 1 =", nummer + 1)

def decrement(nummer = 0):
    print(nummer, "- 1 =", nummer - 1)


berekening()
