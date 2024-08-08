class P1:
    city='Bhopal'
    def display1(self):
        print("this is from display p1")

class P2:
    def display2(self):
        print("this is from display p2")

class C(P1,P2):
    def show(self):
        self.display1()
        self.display2()

obj=C()
obj.show()
print(obj.city)