user_input = int(input())
counter = 0
for x1 in range(user_input + 1):
    for x2 in range(user_input + 1):
        for x3 in range(user_input + 1):
            if x1 + x2 + x3 == user_input:
                counter += 1
print(counter)

