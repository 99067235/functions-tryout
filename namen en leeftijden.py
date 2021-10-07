def namen():
    antwoord = "JA"
    while antwoord == "JA":
            naam = input("Wat is je naam? ")
            leeftijd = input("Wat is je leeftijd? ")
            print("Hallo "+ naam + ", je leeftijd is "+ leeftijd + ".")
            antwoord = input("Wil je nog doorgaan? ").upper()
namen()