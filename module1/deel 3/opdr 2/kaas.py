vraag1 = input('Is de kaas geel? ')

if vraag1 == 'ja':
    vraag2 = input("Zitten er gaten in de kaas? ")
    if vraag2 == 'ja':
        vraag6 = input("Is de kaas belachelijk duur? ")
        if vraag6 == 'ja':
            print("Emmenthaler")
        elif vraag6 == 'nee':
            print('Leerdammer')
        else:
            print('Voer ja of nee in')
    elif vraag2 == 'nee':
        vraag7 = input('Is de kaas hard als steen? ')
        if vraag7 == 'ja':
            print("Parmigiano Reggiano")
        elif vraag7 == 'nee':
            print('Goudse kaas')
        else:
            print('Voer ja of nee in')
    else:
        print('Voer ja of nee in')
        
elif vraag1 == 'nee':
    vraag3 = input('Heeft de kaas blauwe schimmel? ')
    if vraag3 == 'ja':
        vraag4 = input("Heeft de kaas korst? ")
        if vraag4 == 'ja':
            print("Camembert")
        elif vraag4 == 'nee':
            print('Mozzarella')
        else:
            print('Voer ja of nee in')
    elif vraag3 == 'nee':
        vraag5 = input('Heeft de kaas korst? ')
        if vraag5 == 'ja':
            print("Blue de Rochbaron")
        elif vraag5 == 'nee':
            print("Foume d'ambert")
        else:
            print('Voer ja of nee in')
    else:
        print('Voer ja of nee in')
        
else:
    print("Voer ja of nee in")
