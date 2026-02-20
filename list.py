a=int(input("Enter the number of items you want"))
c=list()
for x in range(a):
    b=int(input("Enter the item: "))
    c.append(b)
d=int(input("Enter a number that you want less than"))
for x in c:
    if x<d:
        print(x)
        #It is program of user input list and checking wheather item is less than 5 