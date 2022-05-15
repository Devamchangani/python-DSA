f = open ('F:\python\Python - Basic\Chapter - 9\TEXT-File\poem.txt')
t = f.read()

if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()        