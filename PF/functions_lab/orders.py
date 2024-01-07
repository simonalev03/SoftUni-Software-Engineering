def total_price_of_orders(product: str, quantity: int) -> float:
    if product == 'coffee':
        return quantity * 1.50
    elif product == 'water':
        return quantity * 1.00
    elif product == 'coke':
        return quantity * 1.40
    elif product == 'snacks':
        return quantity * 2


product = input()
quantity = int(input())
result = total_price_of_orders(product, quantity)
print(f"{result:.2f}")
