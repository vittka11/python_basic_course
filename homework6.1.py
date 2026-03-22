import string
letters = string.ascii_letters
range = ["a-c", "a-a", "s-H", "a-A"]
for text in range:
      start, end = text.split("-")
      result = letters [letters.index(start): letters.index(end)+1]
      print(result)