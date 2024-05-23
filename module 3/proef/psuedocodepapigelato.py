# welkom bij papi gelato je mag alle smaken kiezen zolang het maar vanille is
# Stap 1
# De werknemer stelt de vraag aan de klant: "Hoeveel bolletjes wilt u?"
# Aan de hand van het antwoord van de klant worden verschillende acties ondernomen:
# A. bij een aantal van 1 t/m 3 start stap 2.
# B. bij een aantal van 4 t/m 8 sla je stap 2 over en geeft de werknemer het volgende antwoord: "Dan krijgt u van mij een bakje met {aantal} bolletjes".
# C. bij een aantal hoger dan 8 moet de werknemer zeggen: "Sorry, zulke grote bakken hebben we niet" en wordt deze stap herhaald.
# D. anders moet de werknemer zeggen: "Sorry dat snap ik niet..." en wordt deze stap herhaald.

# Stap 2
# De werknemer stelt de vraag aan de klant: "Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?"
# Aan de hand van het antwoord van de klant worden verschillende acties ondernomen:
# A. bij de keuze bakje of hoorntje start stap 3.
# B. anders krijg je de tekst te zien: "Sorry, dat snap ik niet..." en wordt deze stap herhaald.

# Stap 3
# De werknemer zegt: "Hier is uw {hoorntje/bakje} met {aantal} bolletje(s)."
# Daarna stelt de werknemer de vraag aan de klant: "Wilt u nog meer bestellen?"
# A. als de klant ja antwoordt, start stap 1 opnieuw.
# B. als de klant nee antwoordt, zegt de werknemer: "Bedankt en tot ziens!" en stopt het programma.
# C. anders krijg je de tekst te zien: "Sorry, dat snap ik niet..." en wordt deze stap herhaald.