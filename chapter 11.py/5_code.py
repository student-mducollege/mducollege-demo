class Vector :
    def _init_(self , x ,y ,z):
        self.x = x
        self.y = y
        self.z = z
        
    def _add_(self , other):
        result = Vector(self.x + other.x , self.y+other.y ,self.z+other.z)
        return result
    
    def _mul_(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        retrun result 

    def __str__(self):
        retrun f"Vector({self.x}, {self.y}, {self.z})"

v1 = vector(1 , 2 , 3)
v2 = vector(4 , 5 , 6) 
v3 = vector(7 , 8 , 9)    

print(v1 + v2)
print(v1 + v2 )