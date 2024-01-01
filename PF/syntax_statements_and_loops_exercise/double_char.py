while True:
    double_character = ""
    command = input()
    if command == "End":
        break
    elif command == "SoftUni":
        continue
    current_string = command
    for character in current_string:
        double_character += character * 2
    print(double_character)

