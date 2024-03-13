from functions import *
def Getal(vraag:str)-> float:  
    while True:
        try:
           return float(input(vraag))
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een geldig getal in.")


try:
        first_round = True

        while True:
            if first_round:
                print("Wat wilt u doen?")  
            else:
                print(f"Wil je wat met de uitkomst ({result}) doen?")

            keuze = input('''A) getallen optellen
B) getallen aftrekken 
C) getallen vermenigvuldigen
D) getallen delen
E) getal ophogen
F) getal verlagen
G) getal verdubbelen
H) getal halveren?
(of type 'stop' om te stoppen) Kies:''').lower()

            if keuze == 'stop':
                print("Lateerrrrr")
                break
            
            if keuze not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                print("Ongeldige keuze. Probeer het opnieuw.")
                continue

            if first_round:
                n1 = Getal("Voer het eerste getal in: ")
            else:
                n1 = result

            if keuze in ['a', 'b', 'c', 'd']:
                n2 = Getal("Voer het tweede getal in: ")
            
            if keuze == 'a':
                result = addition(n1, n2)
                print(f"{n1} + {n2} = {result}")
            elif keuze == 'b':
                result = subtraction(n1, n2)
                print(f"{n1} - {n2} = {result}")
            elif keuze == 'c':
                result = multiplication(n1, n2)
                print(f"{n1} * {n2} = {result}")
            elif keuze == 'd':
                result = division(n1, n2)
                print(f"{n1} / {n2} = {result}")
            elif keuze == 'e':
                n2 = 1
                result = addition(n1, n2)
                print(f"{n1} + {n2} = {result}")
            elif keuze == 'f':
                n2 = 1
                result = subtraction(n1, n2)
                print(f"{n1} - {n2} = {result}")
            elif keuze == 'g':
                n2 = 2
                result = multiplication(n1, n2)
                print(f"{n1} * {n2} = {result}")
            elif keuze == 'h':
                n2 = 2
                result = division(n1, n2)
                print(f"{n1} / {n2} = {result} ")
            
            first_round = False
except ValueError:
        print("Ongeldige invoer. Voer alstublieft een geldig getal in.")

