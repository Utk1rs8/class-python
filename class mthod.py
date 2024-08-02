class Book:
    price=100
    def details(self,author_name,author_city):
        print("name=",author_name)
        print("city=",author_city)
        print("price=",Book.price)
    @classmethod
    def update_price(clsa,updated_price):
        clsa.price=updated_price
obj=Book()
obj.details("utkarsh","bhopal")
obj.update_price(1500)
obj.details("utkarsh","bhopal")