# Read user input
exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())
# Logic
time_of_exam = exam_hour * 60 + exam_minute
time_of_arriving = arrive_hour * 60 + arrive_minute

if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")
elif time_of_exam - 30 > time_of_arriving:
    print("Early")
difference = abs(time_of_exam - time_of_arriving)
hours = difference // 60
minutes = difference % 60
if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f"{minutes} minutes before the start")
elif time_of_arriving <= time_of_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f"{minutes} minutes after the start")
elif time_of_arriving >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")
# Print output
