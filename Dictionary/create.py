n = int(input("Enter number of students: "))
students = {}
for _ in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print(students)
