nums = [int(num) for num in input().split(", ")]
found_indexes_or_no = map(lambda x: x if nums[x] % 2 == 0 else "no", range(len(nums)))
even_nums_indexes = list(filter(lambda a: a != "no", found_indexes_or_no))
print(even_nums_indexes)