# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# to stop a program use exit() or break
 
student_score = int(input("Enter the students marks: "))

if 90 <= student_score <= 100:
    grade = "A"
elif 80 <= student_score < 90:
    grade = "B"
elif 70 <= student_score < 80:
    grade = "C"
elif 60 <= student_score < 70:
    grade = "D"
elif 0 <= student_score < 60:
    grade = "F"
else:
    grade = "Invalid score"

print("Grade:", grade)

