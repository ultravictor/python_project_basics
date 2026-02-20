import random as r
while True:
    a=str(input("Enter a four digit number: "))
    b=list(a)
    e="123456789"
    c=[]
    cow=0
    bull=0
    for x in range(4):
        c.append(r.choice(e))
    print(c)
    print(b)
    for x in range(0,4):
        if c[x]==b[x]:
           cow+=1 
        else: bull+=1
    print(f"cow={cow} and bull={bull}")
    d=input("Do you want to play again (yes/no)").lower()
    if d!="yes":
        break
    """Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit 
    that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed 
    correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and 
    “bulls” they have. Keep track of the number of guesses the user makes throughout the game and tell the user at the end."""