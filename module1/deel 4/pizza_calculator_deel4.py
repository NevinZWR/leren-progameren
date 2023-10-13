def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")
prijs_small = 8.99
prijs_medium = 12.99
prijs_large = 15.99

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).replace(",","."))
            return value
        except ValueError:
            print("Ongeldige invoer. Voer een komma getal in.")

small_pizza = get_float_input("Hoeveel small pizza's wilt u? ")
medium_pizza = get_float_input("Hoeveel medium pizza's wilt u? ")
large_pizza = get_float_input("Hoeveel large pizza's wilt u? ")

small_pizza_totaal = prijs_small * small_pizza
medium_pizza_totaal = prijs_medium * medium_pizza
large_pizza_totaal = prijs_large * large_pizza

totaal = small_pizza_totaal + medium_pizza_totaal + large_pizza_totaal

print(f"U heeft {small_pizza} small pizza = €{small_pizza_totaal}, "
      f"U heeft {medium_pizza} medium pizza's = €{medium_pizza_totaal}, "
      f"U heeft {large_pizza} large pizza's = €{large_pizza_totaal}. "
      f"Dit komt uit op een totaal van {convertToEuroText(totaal)}.")

