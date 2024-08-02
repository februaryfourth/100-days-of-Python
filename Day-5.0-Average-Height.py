# Input a Python list of student heights
###Example Output 2
##total height = 475
##number of students = 3
##average height = 158

student_heights = [306,200,45]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

student_height = 0

for height in student_heights:
  student_height += height
print(f"total height = {student_height}")

total_students = 0
for students in student_heights:
  total_students += 1
print(f"number of students = {total_students}")

avererage_Students = round(student_height / total_students)
print(f"average height = {avererage_Students}")