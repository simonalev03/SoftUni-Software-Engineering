#Read user input
screening_type = input()
rows = int(input())
columns = int(input())
#Logic
ticket_price = 0
if screening_type == "Premiere":
    ticket_price = 12
elif screening_type == "Normal":
    ticket_price = 7.5
else:
    ticket_price = 5
profit = rows * columns * ticket_price
# Print output
print(f"{profit:.2f} leva")
