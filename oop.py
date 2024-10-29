class Fruits:
    # constructor method
    def __init__(self,price,shape,name):
        self.price=price
        self.shape=shape
        self.name=name
    def display(self):
        print(f"My favorite fruit is {self.name} and its {self.shape} in shape and costs {self.price}")

# create instance of a class

myobject=Fruits(20,"oval","banana")
myobject.display()
