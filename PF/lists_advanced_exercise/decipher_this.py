encrypted_words = input().split()
for word in encrypted_words:
    split_word = [char for char in word]
    first_cyl = ""
    for char in split_word:
        if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" \
                or char == "6" or char == "7" or char == "8" or char == "9" or char == "0":
            first_cyl += char
            split_word.remove(char)
        split_word[1] = split_word[-1]
        print(split_word)
    first_char = chr(int(first_cyl))
