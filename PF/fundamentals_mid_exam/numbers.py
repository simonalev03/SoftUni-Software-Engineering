numbers = [int(number) for number in input().split()]
numbers.sort(reverse=True)
average_number = sum(numbers) // len(numbers)
new_list = []
for number in numbers:
    if number > average_number and len(new_list) <= 4:
        new_list.append(number)

if 1 <= len(new_list) <= 5:
    print(*new_list)
else:
    print("No")