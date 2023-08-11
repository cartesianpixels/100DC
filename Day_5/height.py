student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum_of_height = 0
num_students = 0
for height in student_heights:
    sum_of_height += height
    num_students += 1
print(round(sum_of_height / num_students))