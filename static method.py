#if there is a situation if u dont wanna use the class variable or class method dont want to use then we use static method
class Student:
    city="Bhopal"
    def display(self):
        print("hello")
    @staticmethod
    def show():
        print("thanks for visit")
obj=Student()
obj.display()
obj.show()
print(obj.city)