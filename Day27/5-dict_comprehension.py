import random

# associate the name list with a random score in a dictionary
names=['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score={student:random.randint(1, 100) for student in names}
print(student_score)

# check who passed the exam from the above scores dictionary
passed_students={student:score for (student,score) in student_score.items() if score>60}
print(passed_students)