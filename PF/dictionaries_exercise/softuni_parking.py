registered_cars = int(input())
all_cars = {}
for current_car in range(registered_cars):
    command = input().split()
    activity, name = command[0], command[1]
    if activity == "register":
        if name in all_cars.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            license_plate = command[2]
            all_cars[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
    elif activity == "unregister":
        if name not in all_cars.keys():
            print(f"ERROR: user {name} not found")
        else:
            all_cars.pop(name)
            print(f"{name} unregistered successfully")

for name, license_plate in all_cars.items():
    print(f"{name} => {license_plate}")
