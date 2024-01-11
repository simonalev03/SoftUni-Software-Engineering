def is_palindrome(some_number: str) -> bool:
    if current_number == current_number[::-1]:
        return True
    return False


numbers = input().split(", ")
for current_number in numbers:
    print(is_palindrome(current_number))
