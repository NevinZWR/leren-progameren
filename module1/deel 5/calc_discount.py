from test_lib import test, report

MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    discount_brands = month_discount_brands.split(',')
    if brand in discount_brands:
        discount = round((price * MONTH_DISCOUNT_PERC) / 100, 2)
        return discount
    else:
        return 0.0
   
calc_discount_brands = 'Vespa,Kymco,Yamaha' 

test("korting vespa", 100.0, calc_discount(1000.0, 'Vespa', calc_discount_brands))

test("korting honda", 0.0, calc_discount(800.0, 'Honda', calc_discount_brands))

test("korting kymco", 50.05, calc_discount(500.5, 'Kymco', calc_discount_brands))

test("korting Yamaha", 250.0, calc_discount(2500, 'Yamaha', calc_discount_brands))

test("Korting ABC", 0.0, calc_discount(600.0, 'ABC', calc_discount_brands))

report()
