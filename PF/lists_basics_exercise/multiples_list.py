factor = int(input())
count = int(input())
number_list = []
current_number = factor
while True:
    if current_number % factor == 0:
        number_list.append(current_number)
    if len(number_list) == count:
        break
    current_number += 1
print(number_list)