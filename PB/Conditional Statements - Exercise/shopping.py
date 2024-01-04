#Read user input
budget = float(input())
videocards = int(input())
processors = int(input())
ram_sticks = int(input())

#Logic
videocard_price = 250
total_videocard_price = videocard_price * videocards
processor_price = total_videocard_price * 0.35
ram_stick_price = total_videocard_price * 0.1
end_sum = total_videocard_price + (processor_price * processors) + (ram_stick_price * ram_sticks)
if videocards > processors:
    end_sum *= 0.85
left_budget = abs(budget - end_sum)

if budget >= end_sum:
    print(f"You have {left_budget:.2f} leva left!")
else:
    print(f"Not enough money! You need {left_budget:.2f} leva more!")


#Print output