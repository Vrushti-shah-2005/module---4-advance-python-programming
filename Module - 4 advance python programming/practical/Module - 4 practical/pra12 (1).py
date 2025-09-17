import re

text = "Python programming is fun and powerful."

word = "programming"

match = re.search(word, text)

if match:
    print(f"'{word}' found in the string at position {match.start()}.")
else:
    print(f"'{word}' not found in the string.")
