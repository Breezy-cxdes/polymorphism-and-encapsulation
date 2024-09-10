class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("my name is",self.name,"my age is",self.age)
    def  make_sound(self):
        print("Meow")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("my name is",self.name,"my age is",self.age)
    def make_sound(self):
        print("Bark")

cat1=cat("Kit1cat",1)
dog1=dog("Bruno",2)
for animal in (cat1,dog1):
    animal.info()
    animal.make_sound()
    


    # List of selling prices
selling_prices = [900, 900, 1000]

# Iterate through the prices and print them
for price in selling_prices:
    print(f"Selling Price: {price}")

