class Student:
    school="SHSS" #static variable
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.center_code="101" #static varible
    def display(self):
        Student.grade="10th" #static variable
        print("name= ",self.name)
        print("roll= ",self.roll)
        print("School= ",Student.school)
        print("Center= ",Student.center_code)
        print("grade= ",Student.grade)
        print("city= ",Student.city)
obj=Student("utkarsh",301)
Student.city="bhopal"
obj.display()
print("school",Student.school)

#static variable can be declared outside method, inside constructor , inside the instance method but in the class