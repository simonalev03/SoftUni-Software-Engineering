nums_as_string = input().split()
nums_as_integers = []
for num in nums_as_string:
    nums_as_integers.append(abs(float(num)))
print(nums_as_integers)

