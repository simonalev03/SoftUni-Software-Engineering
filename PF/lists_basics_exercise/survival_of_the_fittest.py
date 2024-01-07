numbers_as_string = input().split()
numbers_to_remove = int(input())
numbers = []
for number in numbers_as_string:
    numbers.append(int(number))

for removed_number in range(numbers_to_remove):
    numbers.remove(min(numbers))
print(*numbers, sep=", ")
