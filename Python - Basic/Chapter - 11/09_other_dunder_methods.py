class number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1


# __sub__ (-)
# __truediv__ (/)
# __floordiv__ (//)

n = number(9)
n1 = number(5)
n2 = number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul) 
print(n)
print(len(n))