MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_DIEREN_DRESSUUR_JAREN = 4
MIN_JONGLEREN_JAREN = 5
MIN_ACROBATIEK_JAREN = 3

lengte = float(input("Hoe lang bent u? "))
gewicht = float(input("Hoeveel weegt u? "))
vrachtwagenrijbewijs = input("Heeft u een vrachtwagen rij bewijs? J/N ")
Certificaat = input('Heeft u Certificaat “Overleven met gevaarlijk personeel? J/N ')
hogehoed = input('Heeft u een hoge hoed? J/N ')
ervaringdieren = int(input("hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
ervaringjongleren = int(input("hoeveel jaar ervaring heeft u met jongleren? "))
ervaringacrobatiek = int(input("hoeveel jaar praktijk ervaring heeft u met acrobatiek? "))

if (
    vrachtwagenrijbewijs == 'J'
    and hogehoed == 'J'
    and MIN_GEWICHT < gewicht < MAX_GEWICHT
    and MIN_LENGTE < lengte < MAX_LENGTE
    and Certificaat == 'J'
    and (
        ervaringdieren >= MIN_DIEREN_DRESSUUR_JAREN
        or ervaringjongleren >= MIN_JONGLEREN_JAREN
        or ervaringacrobatiek >= MIN_ACROBATIEK_JAREN
    )
):
    geschiktheid = "Gefeliciteerd! U mag solliciteren."
else:
    geschiktheid = "Sorry, u voldoet niet aan alle criteria en kunt niet solliciteren."


print(geschiktheid)