nums = [int(num) for num in input().split(", ")]
group_of_tens = []
group_of_twenties = []
group_of_thirties = []
group_of_forties = []
group_of_fifties = []
for current_number in nums:
    if current_number <= 10:
        group_of_tens.append(current_number)
    elif current_number <= 20:
        group_of_twenties.append(current_number)
    elif current_number <= 30:
        group_of_thirties.append(current_number)
    elif current_number <= 40:
        group_of_forties.append(current_number)
    elif current_number <= 50:
        group_of_fifties.append(current_number)
if group_of_tens:
    print(f"Group of 10's: {group_of_tens}")
if group_of_twenties:
    print(f"Group of 20's: {group_of_twenties}")
if group_of_thirties:
    print(f"Group of 30's: {group_of_thirties}")
if group_of_forties:
    print(f"Group of 40's: {group_of_forties}")
if group_of_fifties:
    print(f"Group of 50's: {group_of_fifties}")
