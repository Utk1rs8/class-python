class Student:
    x=10
    y=20
    def __init__(self):
        print(id(self))#selff hold the current object of current class
        print("this is from constructor fun")
    @staticmethod
    def display():
        print("this is from display fun")
obj=Student()
print(id(obj))#same id of object and the self instance
obj2=Student()
print(id(obj2))#same id of object and the self instance
obj.display()
