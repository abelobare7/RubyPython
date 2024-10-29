class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"{self.name} is a person of age {self.age}  and gender is {self.gender}")

# object
myperson=Person("Abel",30,"Male")
myperson.display()
