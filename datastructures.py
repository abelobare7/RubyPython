# list datastructure, changeable

fruits = ["Mangoes", "Bananas", "Pineapple", "Orange"]
fruits[1]="Watermelon"
num=[5,8,1,-3,6,0,15]

print(fruits)
print(f"I love eating {fruits[1]}")

for i in fruits:
    print(i)
print(num)


# tuples datastructure, ordered, immutable, unchangeable
cars=('Suzuki',"Toyota","Nissan","Mercedes")
print(cars)
print(f"I love {cars[2]} cars")

# set datastructures, unordered, not indexed
colors={"yellow","blue","green","white","orange"}
print(colors)

# dictionaries datastructures, mutable, ey value
staff={"name":"Erick","age":"50","salary":"300000"}
print(staff)
print(staff['name'])