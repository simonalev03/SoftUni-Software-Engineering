def calculator(operator: str, a: int, b: int) -> int:
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a // b
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


operator = input()
a = int(input())
b = int(input())
result = calculator(operator, a, b)
print(result)
