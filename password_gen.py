import random as r
a="LAJSFYEFHLASBasjfiowhfamscqwuohcahw872365HI208@#$&832975KDFSFWJ"
b=int(input("Enter the size: "))
c=""
for x in range(b):
    c=c+(r.choice(a))
print("The random generated password is:")
print(c)
