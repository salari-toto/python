from collections.abc import Iterable

# لیست دانش‌آموزان
students = ["علی", "زهرا", "محمد", "رضا"]

# 1) بررسی اینکه آیا students یک Iterable است یا نه
print("آیا students یک Iterable است؟")
print(isinstance(students, Iterable))

# 2) ساخت Iterator از لیست
it = iter(students)

# 3) نمایش سه عضو اول با next()
print("\nسه عضو اول با next():")
print(next(it))
print(next(it))
print(next(it))

print("\nاعضای باقی‌مانده از همان Iterator:")
for student in it:
    print(student)

# 4) چاپ همه‌ی اعضای لیست با حلقه for
print("\nهمه‌ی اعضای students با for:")
for student in students:
    print(student)

# 5) چالش StopIteration با مدیریت خطا
print("\nبررسی StopIteration:")
it2 = iter(students)

try:
    print(next(it2))
    print(next(it2))
    print(next(it2))
    print(next(it2))
    print(next(it2))  
except StopIteration:
    print("Iterator به پایان رسیده است.")
