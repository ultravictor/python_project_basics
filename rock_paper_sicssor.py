import random as rd
def result():
    b=["rock","paper","scissors"]
    while True:
        a=input("Choose ROCK,PAPER,SCISSORS:")
        if a not in b:
            print("wrong option -- choose again")
            continue
        print(f"you choose:{a}")
        c=rd.choice(b)
        print(f"computer choose:{c}")
        if (a=="rock" and c=="scissors") or (a=="paper" and c=="rock") or (a=="scissors" and c=="paper"): 
            print("YOU WON")
        elif a==c:
            print("ITS DRAW")
        else: print("YOU LOSE")
        d=input("Do you want to play again write (yes/no):")
        if d!="yes":
            break
result()