class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : {self.price}")
        print("-------------------------------")

laptop1=Laptop("Dell","Dell Inpire 15",45000)
laptop1.show_details()
laptop2=Laptop("HP","HP Victus",98000);

laptop2.show_details()

