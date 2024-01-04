beginning_interval = int(input())
end_interval = int(input())
magic_number = int(input())

counter = 0
is_found = False

for x in range(beginning_interval, end_interval + 1):
    for y in range(beginning_interval, end_interval + 1):
        counter += 1
        result = x + y
        if result == magic_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")