# Use the open function to read the content of a file!
# f = open('F:\python\Python - Basic\demo.txt', 'r')
f = open('F:\python\Python - Basic\Chapter - 9\TEXT-File\demo.txt') # by defualt the mode is r
# data = f.read()
data = f.read(5) # reads first file character is read
print(data)
f.close()
