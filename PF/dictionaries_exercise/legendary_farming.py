key_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ""
is_obtained = False
while True:
    materials_and_quantity = input().split()
    for current_element_index in range(0, len(materials_and_quantity), 2):
        material = materials_and_quantity[current_element_index + 1].lower()
        quantity = int(materials_and_quantity[current_element_index])
        if material not in key_materials.keys():
            key_materials[material] = 0
        key_materials[material] += quantity
        if key_materials["shards"] >= 250:
            key_materials["shards"] -= 250
            legendary_item = "Shadowmourne"
            is_obtained = True
        elif key_materials["fragments"] >= 250:
            key_materials["fragments"] -= 250
            legendary_item = "Valanyr"
            is_obtained = True
        elif key_materials["motes"] >= 250:
            key_materials["motes"] -= 250
            legendary_item = "Dragonwrath"
            is_obtained = True
        if is_obtained:
            break
    if is_obtained:
        break
print(f"{legendary_item} obtained!")
for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")



