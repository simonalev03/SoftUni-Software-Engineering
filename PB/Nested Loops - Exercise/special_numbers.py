# Read user input
number = int(input())

# Logic
for current_number in range(1111, 9999 + 1):
    current_number_as_string = str(current_number)
    is_current_number_special = True
    for current_digit in current_number_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            is_current_number_special = False
            break
    if is_current_number_special:
        print(current_number_as_string, end=" ")
# Print output