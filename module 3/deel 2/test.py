import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Voorbeeldlijst

for _ in range(10):
    random_item = random.choice(my_list)
    print(random_item)
