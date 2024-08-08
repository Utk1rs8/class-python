class One:
    def add(self,x,y):
        print(x*y)
class Two(One):
    def add(self,x,y):
        return (x+y)
    def show(self):   
        print(self.add(4,5))
        super().add(4,5)
        
obj=Two()
print(obj.add(3,2))
obj.show()