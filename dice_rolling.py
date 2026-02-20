import random as rd
while True:
    a=input("You want to roll the dices (yes/no): ").lower()
    if a=="no":
        break
    elif a!="yes":
        print("Choose only yes/no")
        continue
    b=rd.randint(1,6)
    c=rd.randint(1,6)
    print("The results are :  ")
    print(b,c)
