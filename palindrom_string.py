"""a="racecar"
if a==a[::-1]:
    print("This is palindrome")"""
# second way
#check if both are equel or not
a="racecar"
b=""
for i in a:
    b=i+b
if a==b:
    print(True)
else: print(False)
        