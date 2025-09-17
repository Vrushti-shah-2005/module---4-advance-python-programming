import re

text = "Python programming is fun."

word = "Python"

match = re.match(word, text)

if match:
    print(f"'{word}' matched at the start of the string.")
else:
    print(f"'{word}' did not match at the start of the string.")
