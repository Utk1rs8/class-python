# class Student:
#     x=10
#     y=20
#     def __init__(self):
#         print(id(self))#selff hold the current object of current class
#         print("this is from constructor fun")
#     @staticmethod
#     def display():
#         print("this is from display fun")
# obj=Student()
# print(id(obj))#same id of object and the self instance
# obj2=Student()
# print(id(obj2))#same id of object and the self instance
# obj.display()

class Student:
    x=10
    y=20
    def __init__(self,x):
        print("this is from constructor fun")
    def __init__(self,x,y):
        print("this is from constructor fun")
    def __init__(self,x,y,z):#only this constructor will run as the last constructor of the class will execute and it will be overwrite
        print("this is from constructor fun")#we can pass n-number of argument in constructor there is no limitation

obj=Student(3,7,5)