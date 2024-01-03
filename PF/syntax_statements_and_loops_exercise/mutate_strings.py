start_string = input()
end_string = input()
last_printed_string = start_string
for current_index in range(len(end_string)):
    left_part = end_string[:current_index + 1]
    right_part = start_string[current_index + 1:]
    final_string = left_part + right_part
    if final_string == last_printed_string:
        continue
    print(final_string)
    last_printed_string = final_string