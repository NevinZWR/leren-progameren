import math
from test_lib import test, report

def calculate_cilinder_content(diameter, hoogte):
    inhoud = (diameter / 2) ** 2 * math.pi * hoogte
    inhoud = round(inhoud, 1)
    return inhoud

test_data = [
    (8.0, 5.0, 251.3),
    (11.0, 7.0, 665.2),
    (18.0, 7.0, 1781.3),
    (15.0, 2.0, 353.4),
    (0.0, 6.0, 0.0)
]

for diameter, hoogte, expect_content in test_data:
    calculated_content = calculate_cilinder_content(diameter, hoogte)
    name = f'test diameter: {diameter} height: {hoogte}'
    test(name, expect_content, calculated_content)

    report()

