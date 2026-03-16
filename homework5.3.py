import string
text = input()
for ch in string.punctuation:
    text = text.replace(ch, "")
hashtag = "#" + "".join(word.capitalize() for word in text.split())
print(hashtag[:140])