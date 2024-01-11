def smallest_number(some_numbers: list) -> int:
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_element = smallest_number([first_number, second_number, third_number])
print(smallest_element)