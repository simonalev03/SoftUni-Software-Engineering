yearly_basketball_tax = int(input())

basketball_shoes = yearly_basketball_tax * (60 / 100)
basketball_wear = basketball_shoes * (80 / 100)
ball = basketball_wear - (basketball_wear * ( 75 / 100))
basketball_accessories = ball - (ball * (80 / 100))

result = yearly_basketball_tax + basketball_shoes + basketball_wear + ball + basketball_accessories

print(result)
