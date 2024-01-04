# Read user input

# Logic
min_number = int(input())
while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num < min_number:
        min_number = num


# Print output
print(min_number)