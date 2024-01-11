def is_number_perfect(some_number):
    numbers_sum = 0
    for current_number in range(1, some_number):
        if some_number % current_number == 0:
            numbers_sum += current_number
    if numbers_sum == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
result = is_number_perfect(number)
print(result)
