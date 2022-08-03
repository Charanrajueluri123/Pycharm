'''list=[1,2,"charan"]
print(len(list))
list.append("gaman")
print(list)
list.remove('charan')
print(list)
list.append("charan")
print(list[1:3])'''

'''list=[1,2,3,4,"chs",'dfsd']
print(list[:4])
print(list[2:])
list.insert(2,'gaman')
print(list)
list2=["mango",'banana','cheryyy']
list.extend(list2)
print(list)
list.remove("mango")
print(list)'''

'''s='charan'
print(s.center(15,"*"))
print(s.capitalize())
print(len(s))'''

'''n=int(input("enter number"))
c=0
for i in range(1,n+1):
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        print(i)'''


class Vehicle:
    def __init__(self, a=50):
        self.a= a

    def seating_capacity(self):
        return self.a


class Bus(Vehicle):
    def __init__(self):
        print("Bus capacity in Vehicle by default")
        super().__init__()

ch = Bus()
print(ch.seating_capacity())
