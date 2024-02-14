import random
from fruitmand import fruitmand
hvlfruit = int(input("hoeveel fruit wilt u ?"))

for x in range(hvlfruit):
    hvlfruit = random.choice(fruitmand)['name']
    print(hvlfruit)