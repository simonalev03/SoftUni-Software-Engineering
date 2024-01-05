start_character_index = int(input())
end_character_index = int(input())
for character in range(start_character_index, end_character_index + 1):
    print(chr(character), end=" ")
