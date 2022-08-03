import math


class p1:
    def __init__(self,a,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        if self.b!=0 and self.c==0 :
            print("Perimeter of the Rectangle:",(2*(self.a+self.b)))
        elif self.b!=0 and self.c!=0 :
            print("Perimeter of the Triangle:", (self.a + self.b + self.c))
        else:
            print("Perimeter of the Circle:", (math.pi *2*self.a))


    def Area(self):
        if self.b!= 0 and self.c==0 :
            print("Area of the Rectangle:",(self.a*self.b))
        elif self.b != 0 and self.c != 0:
            s = self.a + self.b + self.c
            print("Area of the Triangle:", (math.sqrt((s * (s - self.a) * (s - self.b) * (s - self.c)))))
        else:

            print("Area of the Circle:", (math.pi * self.a * self.a))


obj1 = p1(10)
obj1.perimeter()
obj1.Area()
ch = p1 (10,20)
ch.perimeter()
ch.Area()
p = p1 (10,20,30)
p.perimeter()
p.Area()





