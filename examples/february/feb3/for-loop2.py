#Author: Justin C
grade_total = 0

for i in range(3):
    while True:
        grade = int(input("Enter grade: "))
        if(grade >=0 and grade <= 100):
            break
        else:
            print("Invalid grade")
    grade_total += grade

grade_avg = grade_total / 3
print(f"Your average is: {round(grade_avg,1)}")
