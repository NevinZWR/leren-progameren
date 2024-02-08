total_sum = 0
current_number = 50
iteration = 1

while total_sum <= 1000:
    total_sum += current_number
    print(f"{iteration}. {' + '.join(map(str, range(50, current_number + 1)))} = {total_sum}")
    current_number += 1
    iteration += 1
