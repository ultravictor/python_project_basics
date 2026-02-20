def prime(a):
    count=0
    for x in range(2,a+1):
        if a%x==0:
            count+=1
    if count ==1:
        print("Prime")
    else: print("Not prime")
b=int(input("Enter a number to check wheater it is prime or not: "))
prime(b)#this is the code of finding prime number 