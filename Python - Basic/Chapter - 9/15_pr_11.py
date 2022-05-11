import os
oldname = "F:\python\Python - Basic\TEXT-File/copy.txt"
newname = "F:\python\Python - Basic\TEXT-File/rename.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)