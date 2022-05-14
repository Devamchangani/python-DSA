class C2dvect:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self) -> str:
        return f"{self.icap}k + {self.jcap}j"

class C3dvect(C2dvect):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
            return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dvect(1,3)
v3d = C3dvect(5, 8, 7)
print(v2d)
print(v3d) 