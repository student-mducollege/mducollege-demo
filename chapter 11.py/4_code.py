class complex:
    def _init_(self, r, i):
        self.r = r
        self.i = i

    def _add_(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def _str_(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1+c2)       