# Author: Justin Chisholm

assignments = float(input("Assignments: "))
exercises = float(input("Exercises: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))

class_grade = assignments *.55 + exercises*.15 + midterm*.15 + final*.15 

print(f"Your class grade is: {round(class_grade, 1)}%.")
letter = "F"

#grade breakdown
if class_grade >89.5: 
    letter = "A"
elif class_grade>79.5:
    letter = "B"
elif class_grade >69.5:
    letter = "C"
elif class_grade <59.5:
    letter = "D"

print(f"You earned a(n) {letter}.")