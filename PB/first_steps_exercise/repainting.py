quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
hours_needed = int(input())

nylon = 1.50
paint = 14.50
thinner = 5
bags = 0.40

added_nylon = quantity_nylon + 2
added_paint = quantity_paint * 1.1
sum_materials = (added_nylon * nylon) + (added_paint * paint) + (quantity_thinner * thinner) + bags
workers_sum = sum_materials - (sum_materials * (70 / 100))
final_sum = sum_materials + workers_sum * hours_needed
print((round(final_sum, 2)))
