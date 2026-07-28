students = ("علی", "زهرا", "محمد", "علی", "رضا")
print(students)
print(len(students))
print(students[2])
print("محمد" in students)
print(students.count("علی"))
print(students.index("رضا"))
print(students[:2])

for student in students:
    print(student)

students_list = list(students)
students_list.append("سارا")
name = input("نام را وارد کنید: ")

if name in students:
    print(students.index(name))
else:
    print("این نام در تاپل وجود ندارد.")
