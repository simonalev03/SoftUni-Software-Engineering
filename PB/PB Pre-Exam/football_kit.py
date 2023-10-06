shirt_price = float(input())
sum_needed_for_ball = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = 2 * (shorts_price + shirt_price)
sum = shorts_price + socks_price + shoes_price + shirt_price
discount_sum = sum * 0.85
diff = abs(discount_sum - sum_needed_for_ball)

if discount_sum >= sum_needed_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discount_sum:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")