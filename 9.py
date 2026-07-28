with open("students.txt", "w", encoding="utf-8") as file:
    file.write("علی\n")
    file.write("زهرا\n")
    file.write("محمد\n")

print("اطلاعات اولیه فایل:")
with open("students.txt", "r", encoding="utf-8") as file:
    print(file.read(), end="")

new_student = input("نام دانش‌آموز جدید: ")

with open("students.txt", "a", encoding="utf-8") as file:
    file.write(new_student + "\n")

print("اطلاعات جدید فایل:")
with open("students.txt", "r", encoding="utf-8") as file:
    print(file.read(), end="")

print("نام‌های شماره‌گذاری‌شده:")
with open("students.txt", "r", encoding="utf-8") as file:
    for number, name in enumerate(file, start=1):
        print(f"{number}- {name.strip()}")
