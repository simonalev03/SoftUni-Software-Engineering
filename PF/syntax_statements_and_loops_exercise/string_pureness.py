number_of_strings = int(input())
for current_string in range(number_of_strings):
    string_content = input()
    if "_" in string_content or \
            "," in string_content or \
            "." in string_content:
        print(f"{string_content} is not pure!")
    else:
        print(f"{string_content} is pure.")
