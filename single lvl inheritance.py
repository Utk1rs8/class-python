class P:
    city="Bhopal"
    def display(self):
        print("This is from display")
class C(P):
    def show(self):
        print("this is from show")
        print("city",P.city)
obj=C()
obj.show()
print(obj.city)
obj.display()