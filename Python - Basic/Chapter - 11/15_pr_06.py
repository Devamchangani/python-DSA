class complex:
    def __init__(self, r, i, f):
        self.real = r 
        self.imaginary = i
        self.fact = f 

    def __add__(self, c):
        return complex(self.real + c.real, self.imaginary +c.imaginary, self.fact + c.fact)

    def __str__(self):
        return f"{self.real}i + {self.imaginary}j + {self.fact}k"

c1 = complex(1, 4, 9)
c2 = complex(8, 5, 10)
print(c1)
print(c2)
print(c1+c2) 