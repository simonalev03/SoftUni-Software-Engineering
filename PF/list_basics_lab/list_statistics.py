total_numbers = int(input())
positive_list = []
negative_list = []
negative_number_sum = 0
for number in range(total_numbers):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
    else:
        negative_number_sum += current_number
        negative_list.append(current_number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {negative_number_sum}")