number_of_electrons = int(input())
number_of_shells = []
for shell_position in range(1, number_of_electrons + 1):
    current_shell_capacity = 2 * (shell_position**2)
    if current_shell_capacity <= number_of_electrons:
        number_of_shells.append(current_shell_capacity)
        number_of_electrons -= current_shell_capacity
    else:
        number_of_shells.append(number_of_electrons)
        break
print(number_of_shells)