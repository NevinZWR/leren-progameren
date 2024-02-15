import re

def get_sub_sentences(text: str) -> list:
    # Vervang alle scheidingstekens door het teken "|"
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    # Split de tekst op het teken "|"
    sub_sentences = marked_text.split("|")
    return [sentence.strip().lower() for sentence in sub_sentences if sentence.strip()]

def calculate_ego_score(sub_sentences: list) -> int:
    ego_score = 0
    for sentence in sub_sentences:
        words = sentence.split(' ')
        # Controleer of de eerste twee woorden van de zin gelijk zijn aan "ik" of "mijn"
        if len(words) >= 2 and (words[0] == 'ik' or words[0] == 'mijn' or words[1] == 'ik' or words[1] == 'mijn'):
            ego_score += 1
    return ego_score

# Voorbeeldgebruik van de functies:
text = "Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij."
sub_sentences = get_sub_sentences(text)
ego_score = calculate_ego_score(sub_sentences)
print(ego_score)  # Output: 4
