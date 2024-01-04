# Read user input
budget = float(input())
statists = int(input())
clothing = float(input())

# Logic
decor = budget * 0.1
if statists > 150:
    clothing *= 0.9
spending = decor + (clothing * statists)
result = abs(budget - spending)
# Print output
if spending > budget:
    print("Not enough money!")
    print(f"Wingard needs {result:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {result:.2f} leva left.")