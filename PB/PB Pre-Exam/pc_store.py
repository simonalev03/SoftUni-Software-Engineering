# Read user input
processor_price = float(input())
gpu_price = float(input())
ram_stick_price = float(input())
number_of_ram_sticks = int(input())
discount_percent = float(input())


# Logic

processor_price_in_lv = processor_price * 1.57
gpu_price_in_lv = gpu_price * 1.57
ram_stick_price_in_lv = ram_stick_price * 1.57
all_ram_price = ram_stick_price_in_lv * number_of_ram_sticks
processor_discount = processor_price_in_lv * discount_percent
gpu_discount = gpu_price_in_lv * discount_percent
final_price_processor = processor_price_in_lv - processor_discount
final_price_gpu = gpu_price_in_lv - gpu_discount


money_needed_in_lv = final_price_processor + final_price_gpu + all_ram_price
# Print output
print(f"Money needed - {money_needed_in_lv:.2f} leva.")