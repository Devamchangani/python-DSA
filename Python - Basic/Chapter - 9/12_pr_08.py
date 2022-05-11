with open('F:\python\Python - Basic\TEXT-File/this.txt') as f:
    content = f.read()

with open('F:\python\Python - Basic\TEXT-File\copy.txt', 'w') as f:
    f.write(content)