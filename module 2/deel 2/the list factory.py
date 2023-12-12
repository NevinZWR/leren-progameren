def generate_lists():
    hoeveel_lijstjes = int(input("Hoeveel lijstjes? "))
    alle_lijstjes = []

    for i in range(hoeveel_lijstjes):
        lengte = int(input(f"Hoeveel in lijst {i + 1}? "))
        lijstjes = [t * (i + 1) for t in range(1, lengte + 1)]
        alle_lijstjes.append(lijstjes)

    return alle_lijstjes

result = generate_lists()
print(result)