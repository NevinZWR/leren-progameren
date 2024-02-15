def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

small_price = 1.25
medium_price = 2.10

amountS = int(input(f'Hoeveel ijsjes van {convertToEuroText(small_price)} wil je bestellen? '))
amountM = int(input(f'En hoeveel ijsjes van {convertToEuroText(medium_price)} wil je bestellen? '))
small_amount = small_price * amountS
medium_amount = medium_price * amountM
totalPrice = small_amount + medium_amount

print(f'Dat is dan {convertToEuroText(totalPrice)} totaal')