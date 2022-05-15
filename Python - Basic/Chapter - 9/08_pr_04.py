with open('F:\python\Python - Basic\Chapter - 9\TEXT-File\demo.txt') as f:
    content = f.read()

content = content.replace("donkey", "^@%$^@")

with open('F:\python\Python - Basic\Chapter - 9\TEXT-File\demo.txt', "w") as f:
    f.write(content)