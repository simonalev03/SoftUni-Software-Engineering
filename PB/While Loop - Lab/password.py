username = input()
password = input()
while True:
    current_password = input()
    if current_password != password:
        continue
    print(f"Welcome {username}!")
    break

