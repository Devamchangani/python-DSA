def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Devam")

a = increment("52")
print(a)
