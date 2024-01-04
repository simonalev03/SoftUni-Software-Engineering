# Read user input

# Logic
max_number = int(input())
while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num > max_number:
        max_number = num


# Print output
print(max_number)