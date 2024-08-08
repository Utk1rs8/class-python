#access modifire in python:
#public 
#private

class Student:
    _school="SHSS" #static variable
    def display(self):
        print(Student._school) #print static varible
class Teacher(Student):
    name=Student._school
    def show(self):
        print("name",Teacher.name)
obj=Teacher()
obj.show()
print(obj._school)
obj2=Student()
obj2.display()