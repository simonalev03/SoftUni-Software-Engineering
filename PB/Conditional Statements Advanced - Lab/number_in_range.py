#Read user input
number = int(input())
#Logic
result = ""
if -100 <= number <= 100 and number != 0:
    result = "Yes"
else:
    result = "No"
#Print output
print(result)