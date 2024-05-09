from help import *

MAX_TICKETS = 30
MAX_VR_VIP_SEAT_TIME = 45
VR_VIP_SEAT_PRICE_PERIOD = 5
TICKET_PRICE = 7.50
VR_VIP_SEAT_PERIOD_PRICE = 0.37
COLA_PRICE = 2.10
POPCORN_PRICE = 2.89

def input_int_with_range(prompt, min_value, max_value):
    return input_int(prompt, min_value, max_value)

def input_yes_no(prompt):
    return input_option(prompt, YES_NO_OPTIONS)

def calculate_total_tickets(nr_tickets):
    return round(nr_tickets * TICKET_PRICE, 2)

def calculate_vr_vip_seats_price(nr_vr_vip_seats, vr_vip_seat_time):
    return round(nr_vr_vip_seats * (vr_vip_seat_time / VR_VIP_SEAT_PRICE_PERIOD * VR_VIP_SEAT_PERIOD_PRICE), 2)

def calculate_total_item(nr_items, price):
    return round(nr_items * price, 2)

def print_receipt_item(item_name, quantity, price):
    total_price = calculate_total_item(quantity, price)
    print(f'{item_name.ljust(25)} {quantity:2} x {price:.2f} = {total_price:.2f}')

print("SPEELHAL-ENTREE-KASSA")
answer = input_yes_no("Wilt u bestellen? (J/N)")

if answer == 'N':
    exit('Nu geen interesse? Tot ziens!')

print('Ik ga u nu vragen wat en hoeveel u wilt...')

nr_tickets = input_int_with_range("Hoeveel personen? (1-30)", 1, MAX_TICKETS)

vr_vip_ordered = input_yes_no("Wilt u ook VR-VIP seats? (J/N)")
if vr_vip_ordered == 'J':
    nr_vr_vip_seats = input_int_with_range("Hoeveel VR-VIP seats? (0-30)", 0, nr_tickets)
    vr_vip_seat_time = input_int_with_range("Hoeveel minuten in de VR-VIP-seats? (5-45)", 5, MAX_VR_VIP_SEAT_TIME)
    vr_vip_seats_price = calculate_vr_vip_seats_price(nr_vr_vip_seats, vr_vip_seat_time)
else:
    nr_vr_vip_seats = 0
    vr_vip_seat_time = 0
    vr_vip_seats_price = 0

nr_cola = input_int_with_range("Hoeveel cola? (0-30)", 0, nr_tickets)
nr_popcorn = input_int_with_range("Hoeveel popcorn? (0-30)", 0, nr_tickets)

vat_invoice = input_yes_no("Wilt u een factuur met BTW specificatie? (J/N)")
company_name = ""
if vat_invoice == 'J':
    company_name = input("Op welke bedrijfsnaam komt de factuur? (Laat leeg om zelf in te vullen)")

total_tickets = calculate_total_tickets(nr_tickets)
total_vr_vip_seats = calculate_vr_vip_seats_price(nr_vr_vip_seats, vr_vip_seat_time)
total_cola = calculate_total_item(nr_cola, COLA_PRICE)
total_popcorn = calculate_total_item(nr_popcorn, POPCORN_PRICE)
total_all = total_tickets + total_vr_vip_seats + total_cola + total_popcorn

print("\n***** SPEELHAL ENTREE BON *****\n")
print_receipt_item("Tickets", nr_tickets, TICKET_PRICE)
if vr_vip_ordered == 'J':
    print_receipt_item("VR-VIP seats", nr_vr_vip_seats, vr_vip_seats_price)
print_receipt_item("Cola", nr_cola, COLA_PRICE)
print_receipt_item("Popcorn", nr_popcorn, POPCORN_PRICE)
print('.' * 33)
print(f'Totaal: {total_all:.2f}')
if vat_invoice == 'J':
    total_vat_H = get_vat_from_amount_incl(total_tickets + total_vr_vip_seats, 'H')
    total_vat_L = get_vat_from_amount_incl(total_cola + total_popcorn, 'L')
    print(f'BTW Hoog (21%): {total_vat_H:.2f}')
    print(f'BTW Laag (9%): {total_vat_L:.2f}')
print('=' * 33)
print(f'Bedrijfsnaam: {company_name}')
print('Bedankt voor de bestelling, veel plezier!')
