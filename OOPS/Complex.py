class Complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def add(self,other):
        return Complex(self.x+other.x,self.y+other.y)
    
    def mult(self,other):
        return (self.x*other.x - self.y*other.y)
    
complex1 = Complex(3, 4)
complex2 = Complex(1, 2)

result=complex1.add(complex2)
print("Sum:", result.x, "+", result.y, "i")

multi=complex1.mult(complex2)
print("multiply: ", multi)

    