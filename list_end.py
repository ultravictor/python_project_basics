import random as r
def first_last_list(a):
    b=[]
    c=[]
    for x in range(1,a+1):
        b.append(r.randint(1,100))
    print("Random list is: ",b)
    c.append(b[0])
    c.append(b[-1])
    print(f"The new sorted list is: ",c)
a=int(input("Enter the size of a list: "))
first_last_list(a)