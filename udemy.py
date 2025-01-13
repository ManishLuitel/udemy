student_heights = input("Input the list of student heights").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#avg height
total_height = 0
for height in student_heights:
  total_height += height

number_of_students = 0
for student in student_heights:
  number_of_students += 1
  

sum_of_total_height = round(total_height / number_of_students)
print(sum_of_total_height)
