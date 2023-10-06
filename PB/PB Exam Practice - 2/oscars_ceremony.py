rent = int(input())

awards = rent * 70 / 100
eating = awards * (85 / 100)
sounding = eating * (50 / 100)
expenses = rent + awards + eating + sounding
print(f"{expenses:.2f}")