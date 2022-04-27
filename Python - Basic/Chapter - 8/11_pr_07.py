def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "      I am a coder        "
n = remove_and_split(this, "coder")
print(n)
# print(this)
# print(this.strip())