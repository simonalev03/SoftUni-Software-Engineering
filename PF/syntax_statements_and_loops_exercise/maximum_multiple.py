divisor = int(input())
boundary = int(input())
largest_number = 0
for number in range(divisor, boundary + 1):
    if number % divisor == 0:
        if number <= boundary:
            if number > 0:
                largest_number = number
print(largest_number)