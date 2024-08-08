#Those variable whose value changes as a new object is created
#instance variable through constructor
# class Student:
#     def __init__(self,name,age):
#         self.name1=name  #here self.name is instance variable
#         self.age1=age  #here self.age is instance variable 
#     def display(self):
#         print("name =",self.name1)
#         print("age =",self.age1)
# obj=Student("utkarsh",20)
# obj.display()
# print(obj.name1)  #for accessing the instance variable outside the class
# print(obj.age1)
# obj2=Student("pur",21)
# obj2.display()

#instace variable declare through object
# class Student:
#     def __init__(self):
#         pass
#     def display(self):
#         print("name =",self.name1)
#         print("age =",self.age1)
# obj=Student()
# obj.name1="utkarsh"
# obj.age1=20
# obj.display()
# print(obj.name1)  #for accessing the instance variable outside the class
# print(obj.age1)


#instance variable through instance method
class Student:
    def display(self,name,age):
        self.name1=name #declaring instance variable
        self.age1=age
    def show(self):
        print(self.name1,self.age1)
obj=Student()
obj.display("utkarsh",20)
obj.show()
print(obj.name1,obj.age1)  #for accessing the instance variable outside the class

#-------------------------------------------------------------------------------------------------------------

#access instance variable :- 1> within the class ->through self 
#                            2> outside of the class-> through object