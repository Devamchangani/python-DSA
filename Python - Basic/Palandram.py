
def pal(str):
    if str == str[::-1]:
        return True
    else:
        return False


print(pal("helleH"))