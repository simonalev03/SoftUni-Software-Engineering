word = input()
some_dict = {}
for char in word:
    if char not in some_dict.keys() and char != " ":
        some_dict[char] = 1
    elif char in some_dict.keys() and char != " ":
        some_dict[char] += 1
for char, count in some_dict.items():
    print(f"{char} -> {count}")