user_input = input()
a = 1
e = 2
i_points = 3
o = 4
u = 5
sum = 0
for i in range(len(user_input)):
    char = user_input[i]
    if char == "a":
        sum += a
    elif char == "e":
        sum += e
    elif char == "i":
        sum += i_points
    elif char == "o":
        sum += o
    elif char == "u":
        sum += u
print(sum)
