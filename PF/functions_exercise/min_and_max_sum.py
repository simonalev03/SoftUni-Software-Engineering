def min_max_and_sum_numbers(some_numbers: list):
    return min(some_numbers), max(some_numbers), sum(some_numbers)


numbers_as_string = input().split()
numbers_as_integers = []
for current_number in numbers_as_string:
    numbers_as_integers.append(int(current_number))
min_number, max_number, sum_numbers = min_max_and_sum_numbers(numbers_as_integers)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
