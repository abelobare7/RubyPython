# while loop

num=5
while num<15:
    print(f"Loop: {num}")
    if num==8:
        break
    num+=1


num1=5
while num1<7:
    num1+=1
    if num1==4:
        continue
    print(f"Looping: {num1}")


# for loop
fruits=["Mangoes","Banana","Oranges","Pineapples"]

for i in fruits:
    print(i)

mycollege="eMobilis M.T.A"

for my in mycollege:
    print(my)