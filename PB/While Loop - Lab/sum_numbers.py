num = int(input())
sum = 0

while True:
    numbers = int(input())
    sum += numbers
    if sum >= num:
        print(sum)
        break

