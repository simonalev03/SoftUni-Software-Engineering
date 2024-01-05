number_of_strings = int(input())
searched_word = input()
list_of_strings = []
list_of_desired_strings = []
for string_number in range(number_of_strings):
    current_string = input()
    list_of_strings.append(current_string)
    if searched_word in current_string:
        list_of_desired_strings.append(current_string)
print(list_of_strings)
print(list_of_desired_strings)
