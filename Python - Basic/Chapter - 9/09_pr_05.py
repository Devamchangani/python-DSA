words = ["donkey", "kaddu", "jadiya"]


with open('F:\python\Python - Basic\TEXT-File\demo.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "^@%$^@")
    with open('F:\python\Python - Basic\TEXT-File\demo.txt', "w") as f:
        f.write(content)