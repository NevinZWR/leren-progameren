import sys
from time import *
from termcolor import colored

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

def slowprint(text, delay=0.03, kleur='white'):
    for char in text:
        print(colored(char, kleur), end='', flush=True)
        sleep(delay)
    print()

def get_age():
    leeftijd = int(input("Voer je leeftijd in: "))
    return leeftijd

def check_age(leeftijd):
    if leeftijd < 18:
        slowprint("Je bent te jong om dit spel te spelen. Je avontuur eindigt hier. :( ", kleur='red')
        exit_program()

def welcome_message():
    slowprint("Welkom in het bos. Je bent verdwaald. Je moet zo snel mogelijk uit het bos zien te komen door keuzes te maken.", delay=0.05, kleur='green')

def choose_character():
    slowprint("Kies je karakter:", kleur='green')
    slowprint("1. Batman", kleur='yellow')
    sleep(0.5)
    slowprint("2. Peter Pan", kleur='cyan')
    sleep(0.5)
    slowprint("3. De Houthakker", kleur='magenta')
    sleep(0.5)
    slowprint("4. Spiderman", kleur='red')
    sleep(0.5)
    keuze_prompt = colored("Voer het nummer van je keuze in: ", 'green', attrs=['bold'])
    keuze = input(keuze_prompt)

    characters = {
        "1": ("Batman", "yellow"),
        "2": ("Peter Pan", "cyan"),
        "3": ("De Houthakker", "magenta"),
        "4": ("Spiderman", "red")
    }

    if keuze in characters:
        gekozen_karakter, kleur_gekozen = characters[keuze]
        slowprint(f"Je hebt {gekozen_karakter} gekozen!", kleur=kleur_gekozen)
        return gekozen_karakter, kleur_gekozen
    else:
        slowprint("Ongeldige keuze. Probeer het opnieuw.", kleur='red')
        return choose_character()

def make_choice(prompt, options):
    while True:
        keuze = input(prompt)
        if keuze in options:
            return keuze
        else:
            slowprint("Ongeldige keuze. Probeer het opnieuw.", kleur='red')

def make_choice_with_delay(prompt, options, delay=0.5):
    slowprint(prompt, kleur='green')
    sleep(delay)
    for option in options:
        slowprint(option, kleur='yellow')
        sleep(delay)
    return make_choice("Voer het nummer van je keuze in: ", options)

def make_decision(prompt, options):
    slowprint(prompt, kleur='green')
    sleep(0.5)  
    return make_choice(prompt, options)

def maak_eenkeuze():
    gekozen_karakter, kleur_gekozen = choose_character()
    welcome_message()

    choices = {
        "1": "Steek de brug over",
        "2": "Ga door het water"
    }

    gekozen_keuze = make_choice_with_delay("Kies uit één van deze 2 keuzes die je kan maken:", choices)
    
    if gekozen_keuze == "1":
        slowprint("Goede keuze! Je hebt de brug veilig overgestoken.", kleur='green')
    elif gekozen_keuze == "2":
        slowprint("Oei, dat was niet zo'n goede keuze. Je hebt het nu koud, dus je kunt niet goed lopen.", kleur='red')

def maak_keuze():
    maak_eenkeuze()
    
    choices = {
        "1": "Ga door de grot",
        "2": "Ga om de grot heen"
    }

    while True:
        keuze3 = input("Voer '1' in om door de grot te gaan of '2' om er omheen te gaan, maaaarrrr, welke keuze maak je? ")
        if keuze3 in ["1", "2"]:
            break
        else:
            slowprint("Ongeldige keuze. Probeer het opnieuw", kleur='red')

    if keuze3 == "1":
        slowprint("Je gaat door de grot en je moet de weg terug vinden.", kleur='green')
        sleep(0.5)
        slowprint("Voer '1' in om de terugweg te vinden of '2' als je de weg niet terug kunt vinden ga je dood: ", kleur='green')
        
        while True:
            keuze4 = input("Welke keuze maak je? ")
            if keuze4 in ["1", "2"]:
                break
            else:
                slowprint("Ongeldige keuze. Probeer het opnieuw", kleur='red')

        if keuze4 == "1":
            slowprint("Goed gedaan! Je hebt de weg teruggevonden en bent veilig uit de grot gekomen.", kleur='green')
        elif keuze4 == "2":
            slowprint("Helaas, je kon de weg niet vinden en bent gestorven in de grot. Je avontuur eindigt hier. :(", kleur='red')
            exit_program()
    elif keuze3 == "2":
        slowprint("Dat was een goede keuze, maar je moet nu wel een stuk omlopen, maar je kan nu in ieder geval niet verdwalen.", kleur='green')

maak_eenkeuze()
slowprint("Je bent om de grot heen gelopen en je bent bij het volgende stuk van het bos.", kleur='green')
slowprint("Je hebt nu komt nu op een kruispunt aan.", kleur='magenta')
slowprint("Je kan links, rechtdoor, of rechts.", kleur='yellow')
slowprint("Links gaat dieper het bos in.", kleur='red')
slowprint("Rechts gaat richting een dorp.", kleur='green')
slowprint("En rechtdoor gaat richting het einde van het bos.", kleur='green')
slowprint("Welke keuze maak je?", kleur='green')

while True:
    keuze5 = input(colored("Voer 'rechts' in om het rechtse pad te kiezen, voer 'links' in om het linkse pad te kiezen, en voer 'rechtdoor' in om rechtdoor te gaan: ", 'green', attrs=['bold']))
    if keuze5 in ["rechts", "links", "rechtdoor"]:
        break
    else:
        slowprint("Ongeldige keuze. Probeer het opnieuw", kleur='red')

gekozen_pad = ""
gekozen_weg = ""

if keuze5 == "rechts":
    gekozen_pad = "rechts"
    gekozen_weg = "richting het dorp"
    slowprint(f"Je hebt het {gekozen_pad} pad genomen. Je gaat nu {gekozen_weg}.", kleur='green')
elif keuze5 == "links":
    gekozen_pad = "linkse"
    gekozen_weg = "dieper het bos in"
    slowprint(f"Je hebt het {gekozen_pad} pad genomen. Je gaat nu {gekozen_weg}.", kleur='red')
elif keuze5 == "rechtdoor":
    gekozen_pad = "rechtdoor"
    gekozen_weg = "richting het einde van het bos"
    slowprint(f"Je hebt het {gekozen_pad} pad genomen. Je gaat nu {gekozen_weg}.", kleur='yellow')

slowprint(f"Je gaat nu {gekozen_pad}.", kleur='green')
slowprint(f"Je komt aan bij {gekozen_weg}.", kleur='yellow')
slowprint("Je gaat even rusten.", kleur='green')
sleep(5)
slowprint("Je hoort allemaal rare geluiden!...", kleur='red')
slowprint("Je denkt ik moet snel weg.", kleur='red')
slowprint("Je gaat verder zonder er bij na te denken.", kleur='red')
slowprint("Je hoort iets achter je aan rennen.", kleur='red')
slowprint("Je gaat ergens rechts en je gaat achter een boom staan.", kleur='green')
slowprint("Je kijkt wat het geluid was.", kleur='red')
slowprint("Het is een beer!...", kleur='red')
slowprint("Je kan nu een keuze maken, of je maakt de beer dood en je kleedt je lekker warm aan of je gaat stiekem weg, zonder dat de beer het weet.", kleur='yellow')
slowprint("Welke keuze maak je?", kleur='green')

while True:
    keuze6 = input(colored("Voer in 'schieten' om de beer dood te maken en lekker warm aan te kleden. Je hebt maar 1 kogel in je wapen, of voer 'rennen' in om weg te komen van de beer: ", 'green', attrs=['bold']))
    if keuze6 in ["schieten", "rennen"]:
        break
    else:
        slowprint("Ongeldige keuze. Probeer het opnieuw.", kleur='red')

if keuze6 == "schieten":
    slowprint("Dat was niet zo'n goede keuze. Je hebt de beer niet goed geraakt. Hij leeft nog en is boos!", kleur='red')
    sleep(1)
    slowprint("Je realiseerde je dat je nog maar één kogel had. Wat ga je doen?", kleur='cyan')
    
    while True:
        keuze7 = input(colored("Voer 'vluchten' in om weg te rennen of 'verstoppen' om je te verstoppen: ", 'green', attrs=['bold']))
        if keuze7 in ["vluchten", "verstoppen"]:
            break
        else:
            slowprint("Ongeldige keuze. Probeer het opnieuw.", kleur='red')

    if keuze7 == "vluchten":
        slowprint("Je rent zo snel als je kunt, maar de beer haalt je in. Het avontuur eindigt hier. :(", kleur='red')
    elif keuze7 == "verstoppen":
        slowprint("Je verstopt je en de beer snuffelt wat rond en lijkt je niet te vinden. Na een tijdje verdwijnt de beer. Dat was close!", kleur='green')
        sleep(1)
        slowprint("Je gaat verder door het bos.", kleur='cyan')

elif keuze6 == "rennen":
    slowprint("Dat was een goede keuze! Je hebt de beer weten te ontlopen.", kleur='green')
    sleep(1)
    slowprint("Je komt nu bij een rivier. Wat wil je doen?", kleur='cyan')

    while True:
        keuze8 = input(colored("Voer 'zwemmen' in om door de rivier te zwemmen of 'omlopen' om langs de rivier te lopen: ", 'green', attrs=['bold']))
        if keuze8 in ["zwemmen", "omlopen"]:
            break
        else:
            slowprint("Ongeldige keuze. Probeer het opnieuw.", kleur='red')

    if keuze8 == "zwemmen":
        slowprint("Je besluit door de rivier te zwemmen. Het is zwaar, maar je haalt de overkant.", kleur='green')
        sleep(1)
        slowprint("Je avontuur gaat verder.", kleur='cyan')
    elif keuze8 == "omlopen":
        slowprint("Je besluit langs de rivier te lopen en komt bij een brug. Wat wil je doen?", kleur='cyan')

        while True:
            keuze9 = input(colored("Voer 'oversteken' in om de brug over te steken of 'omlopen' om langs de rivier te blijven lopen: ", 'green', attrs=['bold']))
            if keuze9 in ["oversteken", "omlopen"]:
                break
            else:
                slowprint("Ongeldige keuze. Probeer het opnieuw.", kleur='red')

        if keuze9 == "oversteken":
            slowprint("Dat was een goeie keuze je bent veilig overgestoken", kleur='green')
            if keuze9 == "omlopen":
                slowprint("Dat was niet zo een goeie keuze je bent nu verdwaald en je kan de weg niet meer terug vinden.",kleur='red')
                exit_program()

    slowprint(f"Je hebt {keuze5} gemaakt.")
slowprint("Je moet nu nog 1 keuze maken om uit het bos te komen.", kleur='green')
slowprint("Onee!.. je komt een slang tegen.", kleur='red')
slowprint("Het is een anaconda!", kleur='red')
slowprint("Als je wordt gebeten ga je dood door het gif in zijn tanden!", kleur='red')
slowprint("Je moet er dus voor zorgen dat je niet wordt gebeten.", kleur='red')
slowprint("Hier komen de keuzes!", kleur='yellow')
slowprint("Of je gaat langs de anaconda zonder dat hij je hoort, of je valt hem aan maar dan riskeer je dat je dood gaat.", kleur='red')

while True:
    keuze10 = input(colored("Voer 'langs' in om langs de anaconda te gaan of voer 'aanvallen' in om de anaconda aan te vallen: ",'red',attrs=['bold']))
    
    if keuze10 == "langs":
        slowprint("Dat was een goede keuze! Je hebt nu het einde van het spel bereikt!", kleur='green')
        break
    elif keuze10 == "aanvallen":
        slowprint("Dat was niet zo'n goede keuze, je bent gebeten en nu ben je dood.", kleur='red')
        exit_program()
    else:
        slowprint("Ongeldige keuze. Probeer het opnieuw.", kleur='red')