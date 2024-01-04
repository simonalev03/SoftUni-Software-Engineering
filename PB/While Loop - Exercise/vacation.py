holiday_price = float(input())
bank_account = float(input())
days_counter = 0
days_spent = 0
is_spending_too_many_days_in_a_row = False

while bank_account < holiday_price:
    action = input()
    spending_money = float(input())
    days_counter += 1
    if action == "spend":
        days_spent += 1
        if days_spent == 5:
            is_spending_too_many_days_in_a_row = True
            break
        bank_account -= spending_money
        if bank_account < 0:
            bank_account = 0
    elif action == "save":
        bank_account += spending_money
        days_spent = 0

if is_spending_too_many_days_in_a_row:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")


