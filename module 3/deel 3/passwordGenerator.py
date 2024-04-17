import random

#alphabetuppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ['@', '#', '$', '%', '&', '_', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



while True:
    password = []
# Random 2 tot 6 hoofdletters
    for i in range(5):
        password.append(random.choice(alphabet).upper())

    # Minimaal 8 kleine letters
    for i in range(12):
        password.append(random.choice(alphabet).lower())

    # 3 speciale tekens
    for i in range(3):
        password.append(random.choice(symbols))

    # Random 4 tot 7 cijfers
    for i in range(4):
        password.append(random.choice(numbers))

    random.shuffle(password)
    if password[12].lower() not in alphabet and password[11].lower() not in alphabet and password[-1] not in alphabet and password[1] not in symbols and password[-1] not in symbols and password[1] not in numbers and password[2] not in numbers and password[3] not in numbers:
        break

wachtwoord = ''.join(password)
print(f"{wachtwoord} heeft {len(wachtwoord)} tekens.")
