class twoDVector:
    def _init_(self,i,j):
     self.i=i
     self.j=j

    def show(self):
        print(f"The vector is {self.i}i+{self.j}j")


class ThreeDVector(twoDVector):
    def _init_(self,i,j,k):
      super()._init_(i,j)  
      self.k=k


    def show(self):
       print(f"The vector is {self.i}i+{self.j}j+{self.k}k")

a=twoDVector(1,2)
a.show()
b=ThreeDVector(1,2,3)
b.show()         


