def grades(grade):
    if grade < 3:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    else:
        return "Excellent"

grade = float(input())
result = grades(grade)
print(result)
