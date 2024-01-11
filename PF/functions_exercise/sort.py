def sorted_numbers(some_numbers: list) -> list:
    return sorted(some_numbers)


numbers = input().split()
numbers_as_integers = []
for current_number in numbers:
    numbers_as_integers.append(int(current_number))
result = sorted_numbers(numbers_as_integers)
print(result)
