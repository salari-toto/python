count = 0

with open("text.txt", "r", encoding="utf-8") as file:
    while True:
        ch = file.read(1)

        if ch == "":
            break

        print(ch)

        if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            count += 1

print("تعداد حروف انگلیسی:", count)
