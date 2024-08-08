class m():
    def add(*n):
        sum=0
        for i in n:
            sum=sum+i
        return(sum)

obj=m
print(obj.add(10,20,30,40))
print(obj.add(10,20))
print(obj.add(10,20,30))