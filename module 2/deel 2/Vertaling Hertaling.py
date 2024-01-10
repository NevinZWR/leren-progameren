text = '''In het hart van de grot zagen ze Draganthor, met zijn glinsterende schubben en vurige ogen. De draak brulde en spuwde een vlammenzee die hen bedreigde, maar Rurik beschermde hen met een krachtig schild van magie.'''

vertalen = {
    "magie": "goud",
    "vurige": "boze",
    "in": "bij",
    "het": "de",
    "hart": "ingang",
    "glinsterende": "ruwe",
    "draak": "Draganthor",
    "De": "",
}

for woord in vertalen:
    text = text.replace(woord, vertalen[woord])

print(text)

