from test_lib import test, report

MONTH_DISCOUNT_PERC = 10

def calc_discount(price, brand, month_discount_brands):
    global MONTH_DISCOUNT_PERC 
    discount_brands = month_discount_brands.split(',')
    for discount_brand in discount_brands:
        if discount_brand.strip() == brand:
            korting = (price * MONTH_DISCOUNT_PERC) / 100
            korting = round(korting, 2)
            return korting
    return 0.0

test_data = [
    (2000.0, 'Kawasaki,Suzuki,Honda', 00.0),
    (1500.0, 'Yamama', 150.0),
    (500.0, 'Vespa', 50.0),
    (1200.0, 'Kymco', 120.0)
]

for price, brand, expected_discount in test_data:
    calculated_discount = calc_discount(price, brand, 'Vespa,Kymco,Yamama')
    name = f'test price: {price} brand: {brand}'
    test(name, expected_discount, calculated_discount)

report()