length = int(input())
width = int(input())
height = int(input())
percent = float(input())

liter_water = 1
volume = length * width * height
free_volume = (volume - (volume * (percent / 100))) * 0.001

print(free_volume)