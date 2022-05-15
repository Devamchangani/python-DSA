with open('F:\python\Python - Basic\Chapter - 9\TEXT-File/this.txt') as f:
    content = f.read()

with open('F:\python\Python - Basic\Chapter - 9\TEXT-File\copy.txt', 'w') as f:
    f.write(content)