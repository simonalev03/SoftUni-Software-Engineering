square_meters_for_greening = float(input())
price_per_square_meter = 7.61
price_for_greening = price_per_square_meter * square_meters_for_greening
discount = price_for_greening * 0.18

discount_price = price_for_greening - discount

result = f"The final price is: {discount_price} lv."
discount = f"The discount is: {discount} ."

print(result)
print(discount)
