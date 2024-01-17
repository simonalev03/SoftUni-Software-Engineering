list_of_words = input().split()
palindrome_word = input()
found_palindromes = []
for word in list_of_words:
    if word == word[::-1]:
        found_palindromes.append(word)
number_of_found_desired_palindromes = found_palindromes.count(palindrome_word)
print(found_palindromes)
print(f"Found palindrome {number_of_found_desired_palindromes} times")