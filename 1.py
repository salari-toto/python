shopping = ["نان", "شیر", "تخم مرغ", "برنج"]
shopping.append("ماست")      # اضافه کردن عضو
shopping.remove("شیر")       # حذف عضو
len(shopping)                # تعداد اعضا
"برنج" in shopping           # بررسی وجود عضو
shopping.sort()               # مرتب‌سازی
print(shopping)              # چاپ فهرست
item = input("نام کالا را وارد کنید: ")

if item in shopping:
    shopping.remove(item)
    print("کالا حذف شد.")
else:
    print("این کالا در لیست وجود ندارد.")
