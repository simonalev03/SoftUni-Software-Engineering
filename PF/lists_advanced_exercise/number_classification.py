all_numbers = [int(num) for num in input().split(", ")]
positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []
for num in all_numbers:
    if num % 2 == 0:
        even_nums.append(num)
        if num >= 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)
    else:
        odd_nums.append(num)
        if num > 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)
positive_nums_as_str = ", ".join([(str(num)) for num in positive_nums])
negative_nums_as_str = ", ".join([str(num) for num in negative_nums])
even_nums_as_str = ", ".join([str(num) for num in even_nums])
odd_nums_as_str = ", ".join([str(num) for num in odd_nums])
print(f"Positive: {positive_nums_as_str}")
print(f"Negative: {negative_nums_as_str}")
print(f"Even: {even_nums_as_str}")
print(f"Odd: {odd_nums_as_str}")