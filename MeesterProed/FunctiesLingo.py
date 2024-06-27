import random
from DataLingo import *

# Selecteer willekeurig een woord
def selecteer_woord():
    return random.choice(WORDS).upper()

# Toon de beginletter van het woord
def toon_beginletter(woord):
    return woord[0]

# Controleer de poging en geef feedback
def controleer_poging(woord, poging):
    feedback = ['_'] * len(woord)
    kleuren = [KLEUR_ROOD] * len(woord)
    woord_lijst = list(woord)
    
    # Check for correct letters in the correct place
    for i in range(len(poging)):
        if poging[i] == woord[i]:
            feedback[i] = poging[i]
            kleuren[i] = KLEUR_GROEN
            woord_lijst[i] = "_"
    
    # Check for correct letters in the wrong place
    for i in range(len(poging)):
        if poging[i] in woord_lijst and kleuren[i] != KLEUR_GROEN:
            feedback[i] = poging[i]
            kleuren[i] = KLEUR_GEEL
            woord_lijst[woord_lijst.index(poging[i])] = "_"
    
    gekleurde_feedback = "".join([kleuren[i] + feedback[i] + KLEUR_RESET for i in range(len(feedback))])
    return gekleurde_feedback

# Grabbelen in de ballenbak
def grabbelen():
    ballenbak = ["Groen", "Groen", "Groen", "Rood", "Rood", "Rood"] + [str(i) for i in range(1, 17)]
    return random.choice(ballenbak), random.choice(ballenbak)

# Update de bingo kaart met de getrokken ballen
def update_bingokaart(bingokaart, bal):
    if bal.isdigit():
        nummer = int(bal) - 1
        row = nummer // 4
        col = nummer % 4
        bingokaart[row][col] = "X"
    return bingokaart

# Controleer of er een winnende lijn op de bingo kaart is
def controleer_bingo(bingokaart):
    # Controleer rijen
    for row in bingokaart:
        if all(cell == "X" for cell in row):
            return True

    # Controleer kolommen
    for col in range(4):
        if all(bingokaart[row][col] == "X" for row in range(4)):
            return True

    # Controleer diagonalen
    if all(bingokaart[i][i] == "X" for i in range(4)) or all(bingokaart[i][3 - i] == "X" for i in range(4)):
        return True

    return False

# Print de bingo kaart
def print_bingokaart(bingokaart):
    print("Bingo Kaart:")
    for row in bingokaart:
        print(" ".join(row))
    print()

# Vraag om een nieuwe poging
def nieuwe_poging(woord, feedback):
    while True:
        print(woord)
        poging = input(f"Poging ({feedback}): ").upper()
        if len(poging) == len(woord) and poging.isalpha():# Check of de poging geldig is
            return poging
        else:
            print(f"Voer een geldig woord van {len(woord)} letters in.")