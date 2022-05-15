with open('F:\python\Python - Basic\Chapter - 9\TEXT-File\log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print("yes python is present")
else:
    print("no python is not present")