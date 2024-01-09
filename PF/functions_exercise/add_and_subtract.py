def sum_numbers(first: int, second: int) -> int:
    return first + second


def subtract(sum_numbers: int, third: int) -> int:
    return sum_numbers - third


def add_and_subtract(first: int, second: int, third: int) -> int:
    num_sum = sum_numbers(first, second)
    num_subtract = subtract(num_sum, third)
    return num_subtract


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)
