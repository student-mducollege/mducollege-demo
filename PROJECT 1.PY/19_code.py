class demo :
    a=4

o=demo()
print(o.a)# print the class attribute because the instance attribute  is not present 
o.a = 0 # Instance attribute is set 
print(o.a)#prints the instance attribut because instance attribute is present 
print(demo.a)#prints the class attribute

