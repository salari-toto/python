scores = [12, 18, 9, 20, 15, 7, 19, 14]

passing_scores = list(filter(lambda x: x >= 10, scores))

print("نمرات قبولی:")
print(passing_scores)
print("تعداد قبول‌شدگان:", len(passing_scores))
