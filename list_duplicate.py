import random as r
def remove(x):
    b=list(set(x))
    print(b)
x=int(input("Enter the size of list: "))
a=[]
for i in range(x):
    a.append(r.randint(1,10))
print("The list with duplicate is: ",a)
print("The new list without duplicate is: ")
remove(a)#this code is about creating a random list and removing the duplicate and returning a new list