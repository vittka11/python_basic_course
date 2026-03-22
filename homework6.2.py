s = int(input())
d, s = divmod(s, 86400)
h, s = divmod(s, 3600)
m, s = divmod(s, 60)
day_word = (
        "день" if d % 10 == 1 and d % 100 != 11 else \
        "дні" if 2 <= d % 10 <= 4 and not (12 <= d % 100 <= 14) else \
        "днів"
)
print(f"{d} {day_word}, {h:02}:{m:02}:{s:02}")