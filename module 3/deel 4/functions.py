def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")