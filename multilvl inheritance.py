class P:
    city='Bhopal'
    def display(self):
        print("this is from display")

class C(P):
    def show(self):
        print("this is from show")
        print("city=",P.city)

class C1(C):
    city1=p=P.city
    def show1(self):
        self.display()
        self.show()
obj=C1()
print(obj.city1)
obj.show1()
obj.show()
obj.display()
print(obj.city)