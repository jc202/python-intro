#Author: Justin CHisholm
from datetime import time

assignments = {
    "Assignment 1" : time(22, 30),
    "Assignment 2" : time(9, 45),
    "Assignment 3" : time(11, 00),
    "Assignment 4" : time(12, 59),
    "Assignment 5" : time(8, 00)
}

for assignment in assignments:
    my_time = assignments[assignment]
    print(f"{assignment}, due {my_time.strftime('%I:%M %p')}")