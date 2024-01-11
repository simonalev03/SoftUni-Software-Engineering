def is_password_valid(some_password: str):
    list_of_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digit_counter = 0
    for current_symbol in some_password:
        if current_symbol.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
   
    return list_of_errors


password = input()
validated_password = is_password_valid(password)
if len(validated_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_password))
