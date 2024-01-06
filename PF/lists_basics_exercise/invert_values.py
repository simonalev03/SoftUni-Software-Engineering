list_of_numbers = input().split()
list_of_opposite_numbers = []
for number in list_of_numbers:
    current_number = -int(number)
    list_of_opposite_numbers.append(current_number)
print(list_of_opposite_numbers)