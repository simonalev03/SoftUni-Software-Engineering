deposit_sum = float(input())
months = int(input())
annual_interest_percent = float(input())
interest = ((deposit_sum * annual_interest_percent) / 100 ) / 12
sum = deposit_sum + months * interest
print(sum)
