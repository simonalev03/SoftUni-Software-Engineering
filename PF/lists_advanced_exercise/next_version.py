software_version = [int(digit) for digit in input().split(".")]

if software_version[2] < 9:
    software_version[2] += 1
else:
    software_version[2] = 0
    if software_version[1] < 9:
        software_version[1] += 1
    else:
        software_version[1] = 0
        software_version[0] += 1

print(f"{software_version[0]}.{software_version[1]}.{software_version[2]}")


