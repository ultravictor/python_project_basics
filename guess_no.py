import random as rd
a=rd.randint(1,9)
count=1
while True:
    b=int(input("Guess a number between (1-9):"))
    if b==a:
        print("CORRECT")
        print(f"you took {count} attempt")
        a=rd.randint(1,9)#Each time the number will chnage 
    elif b>a:
        print(f"your guess is high:")
    elif b<a:
        print(f"your guess is low")
    p=input("Wanna try again (y/n)")
    count+=1
    if p!="y":
        break
