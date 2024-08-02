# Input a list of student scores
student_scores = [40,30,485,384,340,32,3494,3498]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

high_score= 0

for score in student_scores:
  if score > high_score:
    high_score = score
print(f"The highest socre is: {high_score}")