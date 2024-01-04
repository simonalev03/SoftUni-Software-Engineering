# Read user input

user_input = input()

# Logic
prime_numbers = 0
non_prime_numbers = 0
is_number_prime = False
while user_input != "stop":
    number = int(user_input)
    if number < 0:
        print("Number is negative.")
    else:
        is_number_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_number_prime = False
            break
        if is_number_prime:
            prime_numbers += number
        else:
            non_prime_numbers += number
    user_input = input()

# Print output
print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")