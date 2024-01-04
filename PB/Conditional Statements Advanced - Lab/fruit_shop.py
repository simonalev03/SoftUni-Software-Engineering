#Read user input
fruit = input()
day = input()
quantity = float(input())
total_price = 0
is_input_correct = True
#Logic
banana_price_weekday = 2.50
apple_price_weekday = 1.20
orange_price_weekday = 0.85
grapefruit_price_weekday = 1.45
kiwi_price_weekday = 2.70
pineapple_price_weekday = 5.50
grape_price_weekday = 3.85
banana_price_weekend = 2.70
apple_price_weekend = 1.25
orange_price_weekend = 0.90
grapefruit_price_weekend = 1.60
kiwi_price_weekend = 3.00
pineapple_price_weekend = 5.60
grape_price_weekend = 4.20
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        total_price = quantity * banana_price_weekday
    elif fruit == "apple":
        total_price = quantity * apple_price_weekday
    elif fruit == "orange":
        total_price = quantity * orange_price_weekday
    elif fruit == "grapefruit":
        total_price = quantity * grapefruit_price_weekday
    elif fruit == "kiwi":
        total_price = quantity * kiwi_price_weekday
    elif fruit == "pineapple":
        total_price = quantity * pineapple_price_weekday
    elif fruit == "grapes":
        total_price = quantity * grape_price_weekday
    else:
        is_input_correct = False

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        total_price = quantity * banana_price_weekend
    elif fruit == "apple":
        total_price = quantity * apple_price_weekend
    elif fruit == "orange":
        total_price = quantity * orange_price_weekend
    elif fruit == "grapefruit":
        total_price = quantity * grapefruit_price_weekend
    elif fruit == "kiwi":
        total_price = quantity * kiwi_price_weekend
    elif fruit == "pineapple":
        total_price = quantity * pineapple_price_weekend
    elif fruit == "grapes":
        total_price = quantity * grape_price_weekend
    else:
        is_input_correct = False
else:
    is_input_correct = False
#Print output
if is_input_correct == True:
    print(f"{total_price:.2f}")
else:
    print("error")