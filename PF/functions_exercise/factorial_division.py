def factorial_calculation(first: int):
    for current_number in range(1, first):
        first *= current_number
    return first


first_number = int(input())
second_number = int(input())
first_number_factorial = (factorial_calculation(first_number))
second_number_factorial = (factorial_calculation(second_number))
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")
