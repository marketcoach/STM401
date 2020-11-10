ComputeGrade = 'score converted to grade'
print(ComputeGrade.upper())

try:
    score = float(input("Enter a score between 0.0 and 1.0: "))

    if score > 1.0:
        raise Exception("Number Cannot Exceed 1.0")

    if score < 0.0:
        raise Exception("Number Cannot Be Less Than 0.0")

    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"

    print("YOUR GRADE IS: " + grade)
except:
    print("ERROR OCCURED: please enter a score between 0.0 and 1.0 in numbers only")