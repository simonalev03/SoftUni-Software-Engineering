# Read user input
cake_width = int(input())
cake_length = int(input())
whole_cake = cake_width * cake_length
cake_piece = 0
is_cake_enough = False
is_cake_over = False
# Logic
while True:
    user_input = input()
    if user_input == "STOP":
        is_cake_enough = True
        break
    pieces_taken = int(user_input)
    cake_piece += pieces_taken
    if cake_piece >= whole_cake:
        is_cake_over = True
        break

difference = abs(whole_cake - cake_piece)

# Print output
if is_cake_enough:
    print(f"{difference} pieces are left.")
else:
    print(f"No more cake left! You need {difference} pieces more.")