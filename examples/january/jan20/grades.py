# Author: Justin C
#Calculating Class Grade
print("Let's Calculate Your Grade!")
assignments_grade = float(input("Assignments: "))
exercises_grade = float(input("Exercises: "))
midterm_grade = float(input("Midterm: "))
final_grade = float(input("Final: "))

class_grade = assignments_grade * .55 + exercises_grade * .15 + midterm_grade * .15 + final_grade * .15

print(f"Your grade is {round(class_grade, 1)}")

