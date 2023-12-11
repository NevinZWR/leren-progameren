while True:
    try:
        getal = int(input("Voer een getal in voor de tafel: "))
        break
    except ValueError:
        print("vul een getal in")
        
for i in range(1, 11):
    resultaat = i * getal
    print(f"{i} x {getal} = {resultaat}")
