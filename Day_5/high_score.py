student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# get highest score
# we should know all the scores
highest_score = 0
for score in student_scores:
# we should store the highest score so far
    if highest_score < score:
        highest_score = score  
print(f"The highest score in the class is: {highest_score}")