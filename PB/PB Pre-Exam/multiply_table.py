number = int(input())
first_digit = number % 10
number //= 10
second_digit = number % 10
number //= 10
third_digit = number % 10
number //= 10

for i in range(first_digit + 1):
    if i <= 0:
        continue
    for k in range(second_digit + 1):
        if k <= 0:
            continue
        for l in range(third_digit + 1):
            if l <= 0:
                continue
            result = i * k * l
            print(f"{i} * {k} * {l} = {result};")
