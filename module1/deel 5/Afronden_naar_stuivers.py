from test_lib import test, report
from decimal import Decimal, ROUND_HALF_UP

def round_to_stuivers(bedrag):
    bedrag = Decimal(str(bedrag))
    afgerond_bedrag = bedrag.quantize(Decimal('0.05'), rounding=ROUND_HALF_UP)
    return float(afgerond_bedrag)

test_data = [2.24, 13.01, 9.95, 4.78, 6.62]

for origineel_bedrag in test_data:
    afgerond_bedrag = round_to_stuivers(origineel_bedrag)
    name = f'test origineel bedrag: {origineel_bedrag}'
    test(name, afgerond_bedrag, origineel_bedrag)

report()

