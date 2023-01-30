# WAP to change score into Grading system according to the table below:
# 91-100: Outstanding
# 81-90: Exceeds Expectations
# 71-80: Acceptable
# 70 or lower: Fail

student_scores={
    'Harry': 81,
    'Ron': 78,
    'Hermin': 99,
    'Draco': 74,
    'Nevil': 62
}

student_grades={}
for student in student_scores:
    if (student_scores[student]>90):
        student_grades[student]='Outstanding'
    elif (student_scores[student]>80):
        student_grades[student]='Exceeds Expectations'
    elif (student_scores[student]>70):
        student_grades[student]='Acceptable'
    else:
        student_grades[student]='Fail'

for student in student_scores:
    print(f"{student} \t {student_scores[student]} \t {student_grades[student]}")