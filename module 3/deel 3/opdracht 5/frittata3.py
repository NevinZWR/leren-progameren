from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('''ingredienten voor hoeveel personen?
''') # replace this with better input



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
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, TXT_PERSONS)}')
print('-----------------------------------------------')
print(f"*{total_eggs} {str_single_plural(total_eggs, TXT_EGGS)} ") # print eieren
print(f"*{str_amount_fraction(total_milk)} {str_single_plural(total_milk, TXT_CUPS)} {TXT_MILK}({int(ML_CUP * total_milk)} ml)") # print melk
print(f"*{str_amount_fraction(total_salt)} {str_single_plural(total_salt, TXT_TEASPOONS)} {TXT_SALT}({float(total_salt * GRAM_SALT)} gram)") # print zout
print(f"*{str_amount_fraction(total_pepper)} {str_single_plural(total_pepper, TXT_TEASPOONS)} {TXT_PEPPER}({float(total_pepper * GRAM_PEPPER)} gram)")# print zwarte peper
print(f"*{str_amount_fraction(total_oil)} {str_single_plural(total_oil, TXT_SPOONS)} {TXT_OIL}({round(float(total_oil * ML_SPOON), 1)} ml)") # print olijfolie
print(f"*{total_onions} {str_single_plural(total_onions, TXT_ONIONS)} ") # print ui
print(f"*{total_garlics} {str_single_plural(total_garlics, TXT_GARLICS)} ") # print knoflook
print(f"*{str_amount_fraction(total_paprikas)} {str_single_plural(total_garlics, TXT_PAPRIKAS)}") # print spinazie
print(f"*{str_amount_fraction(total_spinach)} {str_single_plural(total_spinach, TXT_CUPS)} {TXT_SPINACH}({int(total_spinach * GRAM_SPINAZE)} gram)") # print paprika's
print(f"*{str_amount_fraction(total_cheese)} {str_single_plural(total_cheese, TXT_CUPS)} {TXT_CHEESE}({int(total_cheese * GRAM_CHEESE)} gram)") # print kaas
print('-----------------------------------------------')
