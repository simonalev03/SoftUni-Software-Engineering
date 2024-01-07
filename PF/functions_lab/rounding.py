def round_nums(number):
    rounded_nums.append(round(number))


nums_as_string = input().split()
nums_as_int = []
for num in nums_as_string:
    nums_as_int.append(float(num))
rounded_nums = []
for number in nums_as_int:
    round_nums(number)
print(rounded_nums)
