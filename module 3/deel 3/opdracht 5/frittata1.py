from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input('''ingredienten voor hoeveel personen?
''')) # replace this with better input


# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS

# calculate amount_eggs
total_eggs = round_piece(AMOUNT_EGGS * factor)	
# calculate amount_milk
total_milk = round_quarter(AMOUNT_MILK * factor)
# calculate amount_salt
total_salt = round_quarter(AMOUNT_SALT * factor)
# calculate amount_pepper
total_pepper = round_quarter(AMOUNT_PEPPER * factor)
# calculate amount_oil
total_oil = round_quarter(AMOUNT_OIL * factor)
# calculate amount_onions
total_onions = round_piece(AMOUNT_ONIONS * factor)
# calculate amount_garlics
total_garlics = round_piece(AMOUNT_GARLICS * factor)
# calculate amount_spinach
total_spinach = round_quarter(AMOUNT_SPINACH * factor)
# calculate amount_paprikas
total_paprikas = round_piece(AMOUNT_PAPRIKAS * factor)
# calculate amount_cheese
total_cheese = round_quarter(AMOUNT_CHEESE * factor)
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} persoon|personen:')

print('-----------------------------------------------')
print(f"{total_eggs} groot ei|grote eieren: ") # print eieren
print(f"{total_milk} kop|koppen melk") # print melk
print(f"{total_salt} theelepel|theelepels zout") # print zout
print(f"{total_pepper} theelepel|theelepels zwarte peper") # print zwarte peper
print(f"{total_oil} lepel|lepels olijfolie") # print olijfolie
print(f"{total_onions} kleine ui, fijngehakt") # print ui
print(f"{total_garlics} teentjes knoflook, fijngehakt") # print knoflook
print(f"{total_paprikas} rode paprika's, in blokjes gesneden") # print spinazie
print(f"{total_spinach} kop|koppen verse spinazie") # print paprika's
print(f"{total_cheese} kop|koppen geraspte cheddar kaas") # print cheddar kaas
print('-----------------------------------------------')