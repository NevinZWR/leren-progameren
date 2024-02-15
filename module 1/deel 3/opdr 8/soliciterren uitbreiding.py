MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_DIEREN_DRESSUUR = 4
MIN_JONGLEREN = 5
MIN_ACROBATIEK = 3
MIN_SNOR_LENGTE = 10
MIN_HAAR_LENGTE = 20
MIN_GLIMLACH_BREEDTE = 10
MIN_ONDERNEMER_JAREN = 3
MIN_WERKNEMERS = 5

lengte = float(input("Hoe lang bent u? "))
gewicht = float(input("Hoeveel weegt u? "))
vrachtwagenrijbewijs = input("Heeft u een vrachtwagen rijbewijs? J/N ").upper() == "J"
Certificaat = input('Heeft u Certificaat “Overleven met gevaarlijk personeel? J/N ').upper() == "J"
hogehoed = input('Heeft u een hoge hoed? J/N ').upper() == "J"
ervaringdieren = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
ervaringjongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
ervaringacrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
heeft_mbo4_diploma = input("Heeft u een Diploma MBO-4 ondernemen? (J/N) ").upper() == "J"
is_man = input("Bent u een man? (J/N) ").upper() == "J"
is_vrouw = input("Bent u een vrouw? (J/N) ").upper() == "J"
is_anders = not (is_man or is_vrouw)
snor_breedte = 0
haar_lengte = 0
glimlach_breedte = 0

if is_man:
    snor_breedte = int(input("Hoe breed is uw snor in cm? "))
elif is_vrouw:
    haar_lengte = int(input("Hoe lang is uw rood krulhaar in cm? "))
else:
    glimlach_breedte = int(input("Hoe breed is uw glimlach in cm? "))

geschikt = True
redenen_afwijzing = []

if not vrachtwagenrijbewijs:
    geschikt = False
    redenen_afwijzing.append("U heeft geen geldig Vrachtwagen rijbewijs.")

if not hogehoed:
    geschikt = False
    redenen_afwijzing.append("U heeft geen hoge hoed.")

if not (MIN_GEWICHT <= gewicht <= MAX_GEWICHT):
    geschikt = False
    redenen_afwijzing.append("U voldoet niet aan het gewichtscriterium.")

if not (MIN_LENGTE <= lengte <= MAX_LENGTE):
    geschikt = False
    redenen_afwijzing.append("U voldoet niet aan het lengtecriterium.")

if not Certificaat:
    geschikt = False
    redenen_afwijzing.append("U heeft geen certificaat 'Overleven met gevaarlijk personeel'.")

if not (ervaringdieren >= MIN_DIEREN_DRESSUUR or ervaringjongleren >= MIN_JONGLEREN or ervaringacrobatiek >= MIN_ACROBATIEK):
    geschikt = False
    redenen_afwijzing.append("U voldoet niet aan de vereiste ervaring met kunsten.")

if not (heeft_mbo4_diploma or (is_man and snor_breedte > MIN_SNOR_LENGTE) or (is_vrouw and haar_lengte > MIN_HAAR_LENGTE) or (is_anders and glimlach_breedte > MIN_GLIMLACH_BREEDTE)):
    geschikt = False
    redenen_afwijzing.append("U voldoet niet aan aanvullende criteria.")

if geschikt:
    print("Gefeliciteerd! U bent geschikt voor de functie van circusdirecteur voor Circus HotelDeBotel.")
else:
    print("Helaas, u voldoet niet aan de criteria voor de functie van circusdirecteur voor Circus HotelDeBotel.")
    print("Redenen voor afwijzing:")
    for reden in redenen_afwijzing:
        print("- " + reden)

