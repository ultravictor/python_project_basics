import random as r
a=int(input("how long do you want to generate a list:"))
b=[]
for x in range(1,a+1):
    b.append(r.randint(1,100))#this a code for generating random list
print(b)