student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Mina": 99,
    "Tony": 74,
    "Sara": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
