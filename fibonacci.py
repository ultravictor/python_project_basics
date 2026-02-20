def fibbo(a):
    x,y,z=0,1,0
    for i in range(a):
        print(z,end=" ")
        x=y
        y=z
        z=x+y
a=int(input("Enter the size of fibbonaci series: "))
print("The series is:")
fibbo(a)
#This code of fibbonacci series