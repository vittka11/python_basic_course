import string
import keyword

name = input()

if name in keyword.kwlist:
    print(False)
elif name[0].isdigit():
    print(False)
elif name != "_" and set(name) == {"_"}:
    print(False)
else:
    result = True
    for ch in name:
        if ch in string.punctuation.replace("_", "") or ch == " " or ch.isupper():
            result = False
            break
    print(result)