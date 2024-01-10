def sum_of_all_even_and_odd_numbers(first: str):
    odd_sum = 0
    even_sum = 0
    for current_digit in first:
        digit_as_number = int(current_digit)
        if digit_as_number % 2 == 0:
            even_sum += digit_as_number
        else:
            odd_sum += digit_as_number

    return odd_sum, even_sum


number = input()
sum_of_odd_digits, sum_of_even_digits = sum_of_all_even_and_odd_numbers(number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
