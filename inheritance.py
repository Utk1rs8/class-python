class p1:
    def display(self):
        print("p1 class")
class c1(p1):
    def display(self):
        print("c1 class")
obj=c1()
obj.display()