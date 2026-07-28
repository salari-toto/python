library = {
    "books": [
        ("Python", "Ahmadi", 2023),
        ("Network+", "Karimi", 2022),
        ("Python", "Ahmadi", 2023)
    ],
    "subjects": {"Python", "Network", "Programming"}
}
# ۱. نمایش تعداد کتاب‌ها
print(len(library["books"]))

# ۲. چاپ اطلاعات اولین کتاب
print(library["books"][0])

# ۳. نمایش فقط عنوان اولین کتاب
print(library["books"][0][0])

# ۴. اضافه کردن کتاب جدید به لیست
library["books"].append(("Linux", "Rahimi", 2024))

# ۵. اضافه کردن موضوع جدید به مجموعه موضوعات
library["subjects"].add("Security")

# ۶. نمایش تعداد موضوع‌ها
print(len(library["subjects"]))

# ۷. چاپ تمام کتاب‌ها با ساختار حلقه for
for title, author, year in library["books"]:
    print("عنوان:", title)
    print("نویسنده:", author)
    print("سال:", year)
    print("------------------")

# ۸. نمایش تمام موضوع‌ها
print(library["subjects"])

# ۹. بررسی وجود موضوع Python در مجموعه
print("Python" in library["subjects"])
library["manager"] = "Ali Ahmadi"

# ۱۰. چاپ کل دیکشنری برای مشاهده تغییرات نهایی
print(library)
