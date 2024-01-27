first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring = []
index_counter = 0
for word in first_sequence:
    for whole_word in second_sequence:
        if word in whole_word:
            substring.append(word)
            break
print(substring)