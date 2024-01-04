numbers = int(input())
sum = 0
first_element = int(input())
sum += first_element
max_element = first_element
for i in range(numbers - 1):
    number_one = int(input())
    sum += number_one
    if number_one > max_element:
        max_element = number_one
if max_element == sum - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    diff = abs(max_element - (sum - max_element))
    print("No")
    print(f"Diff = {diff}")