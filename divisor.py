a=int(input("Enter a number"))
print(f"The divisor of {a} are:")
for x in range(1,a+1):
    if a%x==0:
        print(x)#this the code for finding divisor of a number