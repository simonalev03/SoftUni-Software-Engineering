n = int(input())

odd_sum = 0
even_sum = 0
for i in range(n):
    num_1 = int(input())
    if i % 2 == 0:
        even_sum += num_1
    else:
        odd_sum += num_1
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {difference}")