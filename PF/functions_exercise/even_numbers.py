list_of_numbers = input().split()
numbers_as_digits = []
for current_number in list_of_numbers:
    numbers_as_digits.append(int(current_number))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)
