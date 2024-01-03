total_coffee = 0
while True:
    command = input()
    if command == "END":
        break
    elif command.lower() == "coding":
        if command.isupper():
            total_coffee += 2
        else:
            total_coffee += 1
    elif command.lower() == "dog" or command.lower() == "cat":
        if command.isupper():
            total_coffee += 2
        else:
            total_coffee += 1
    elif command.lower() == "movie":
        if command.isupper():
            total_coffee += 2
        else:
            total_coffee += 1
if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)