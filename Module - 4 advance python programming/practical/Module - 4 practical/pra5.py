file = open("multilines.txt", "w")

lines = [
    "Python is fun!\n",
    "File handling is easy.\n",
    "We are writing multiple lines into a file.\n"
]

file.writelines(lines)

file.close()

print("Multiple strings written to 'multilines.txt' successfully.")
