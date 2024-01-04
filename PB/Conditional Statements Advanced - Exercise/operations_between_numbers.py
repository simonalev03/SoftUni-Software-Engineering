# Read user input
first_number = int(input())
second_number = int(input())
operator = input()
# Logic
result = 0

if operator == "+" or operator == "-" or operator == "*":
    even_or_odd = ""
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    else:
        result = first_number * second_number
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")

elif operator == "/" or operator == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        if operator == "/":
            result = first_number / second_number
            print(f"{first_number} {operator} {second_number} = {result:.2f} ")
        elif operator == "%":
            result = first_number % second_number
            print(f"{first_number} {operator} {second_number} = {result} ")
# Print output
