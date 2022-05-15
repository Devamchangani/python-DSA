def readfile(filename):
    try:
        with open (filename , "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File{filename} is not found")



readfile("F:\python\Python - Basic\Chapter - 12\Text-File/1.txt")
readfile("F:\python\Python - Basic\Chapter - 12\Text-File/2.txt")
readfile("F:\python\Python - Basic\Chapter - 12\Text-File/3.txt")

