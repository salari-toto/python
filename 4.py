book = {
    "title": "Python",
    "author": "Ahmadi",
    "publisher": "Danesh",
    "year": 2024,
    "pages": 350
}

# 1. نمایش اطلاعات کامل کتاب
print(book)

# 2. نمایش فقط نام کتاب
print(book["title"])

# 3. نمایش تعداد کلیدها
print(len(book))

# 4. تغییر سال انتشار
book["year"] = 2025

# 5. افزودن قیمت
book["price"] = 450000

# 6. حذف کلید publisher
book.pop("publisher")

# 7. نمایش تمام کلیدها
print(book.keys())

# 8. نمایش تمام مقادیر
print(book.values())

# 9. چاپ کلید و مقدار با حلقه for
for key, value in book.items():
    print(key, ":", value)
