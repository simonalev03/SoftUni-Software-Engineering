numbers = int(input())
for number in range(numbers):
    new_number = int(input())
    if new_number % 2 == 1:
        print(f"{new_number} is odd!")
        break
else:
    print("All numbers are even.")