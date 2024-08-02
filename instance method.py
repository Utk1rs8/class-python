class Student:
    city="bhopal"
    def __init__(self,name,roll) -> None:
        self.name=name
        self.roll=roll
    def display(self):
        print("hello this is display instance method")
    def show(self):
        print("name=",self.name)
        print("roll=",self.roll)
        print(Student.city)
        self.display() #for calling any instance method you have to call it with self
obj=Student("utkarsh",101)
obj.show()
# obj.display()