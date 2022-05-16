def greater_then_5(num):
    if num > 5:
        return True
    else:
        return False


l = [1, 54, 85, 99, 6, 7, 4 ]
print(list(filter(greater_then_5, l)))

