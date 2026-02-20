#printing as it is
"""print("Twinkle, twinkle, little star,")
print("	       How I wonder what you are!") 
print("                Up above the world so high,   ")		
print("                Like a diamond in the sky. ")
print("Twinkle, twinkle, little star, ")
print("       How I wonder what you are")"""
#finding current date and time
"""import datetime as t
print(t.datetime.now())"""
#finding area of circle
"""pie=3.14
r=float(input("Enter the radius"))
a=pie*r*r
print(f"the area of circle is{a}")"""
#list generator#tuple generator
"""a=[]
b=int(input("Enter the size of list"))
for x in range(b):
    c=str(input("Enter the list items:"))#you can change if you want to enter string or int or float
    a.append(c)
print(a)
d=tuple(a)
print(d)"""
#extension finder
"""a=str(input("ENter the file name:"))
b=a.split(".")
print(b[-1])"""
#first and last color from given list
"""color_list = ["Red","Green","White" ,"Black"]
print(f"the first color is {color_list[0]}")
print(f"the last color is {color_list[-1]}")"""
#this string format
"""exam_st_date = (11, 12, 2014)
print("the exam will be at: %i/%i/%i"%exam_st_date)"""
#A Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""def cal(n):
    c=int(n)
    a=int(n+n)
    b=int(n+n+n)
    d=a+b+c
    print(d)
n=str(input("Enter a number: "))
cal(n)"""
# Python program to print the documents (syntax, description etc.) of Python built-in function(s).
"""import random
print(random.randint.__doc__)#__doc__ is a method definition"""
#A Python program that prints the calendar for a given month and year.
"""import calendar as c
a=int(input("Enter the year: "))
b=int(input("Enter the month: "))
print(c.month(a,b))"""
#A Python program to calculate the number of days between two dates.
"""import math
a=(2014, 7, 2)#It is long and not efficient in every way
b=(2014, 7, 11)
c=[]
for x in range(0,3):
    c.append(abs(a[x]-b[x]))
day=(c[0]*365)+(c[1]*30)+c[2]
print(day)"""
"""from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)"""
#A Python program to get the volume of a sphere with radius.
"""def sphere_volume(r):
    pie=3.14
    v=4.0/3.0*pie*r**3
    print(f"The volume of sphere is: {v:.2f}")
r=float(input("Enter the radius of sphere: "))
sphere_volume(r)"""
#A Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""import math
a=int(input("enter a number: "))
b=0
if a>17:
    b=2*(a-17)
    print(f"Your number is greater than 17 and result is {b}")
else:print(f"your number is not greater than 17 and result is{17-a}")"""
#A Python program to test whether a number is within 100 of 1000 or 2000
"""a=int(input("Enter a number: "))
if (900<=a<=1000) or (1900<=a<=2100):#logic
    print(True)
else: print(False)"""
#A Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""def cal(a,b,c):
    if a==b==c:
        print(f"The values are same so the answer is: {3*(a+b+c)}")
    else:print(f"The values are not same so answer is: {a+b+c}")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
cal(a,b,c)"""
#A Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""a=str(input("Enter a string: "))
if len(a)>=2 and a[:2]=="Is":
    print(a)
else: print("Is"+a)"""
#A Python program that returns a string that is n (non-negative integer) copies of a given string.
"""a=str(input("Enter a word: "))
b=int(input("Tell me number of times you want to copy: "))
c=""
for x in range(b):
    c=c+a
print(c)"""
#A Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""a=int(input("enter a number: "))
if a%2==0:
    print("Even number")
else: print("Odd number")"""
#A Python program to count the number 4 in a given list
"""import random as r
a=int(input("enter the size of list:"))
b=[]
count=0
for x in range(a):
    b.append(r.randint(1,10))
print(b)
for x in b:
    if x==4:
        count+=1
print(f"The number of times 4 is obtained in list is {count}")"""
#A Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
"""import math
b=str(input("Enter a word:"))
a=abs(int(input("How many times you want to copy:")))
c=""
for x in range(a):
    if len(b)>=2 :
        c=c+b[:2]
print(f"your string is {b}")
print(c)"""
#A Python program to test whether a passed letter is a vowel or not.
"""a=str(input("Enter a alphabet:"))
b="aeiou"
if a in b:
    print("It is vowel")
else:print("It is consonent")"""
#A Python program that checks whether a specified value is contained within a group of values.
"""import random as r
a=int(input("Enter the size of list:"))
b=[]
for x in range(a):
    b.append(r.randint(1,9))
c=int(input("Enter the value you want search:"))
if c in b:
    print("Its exists")
else:print("does not exists")"""
#A Python program to create a histogram from a given list of integers.
"""a=int(input("enter the size of list: "))
b=[]
for x in range(a):
    b.append(int(input("enter the items in list: ")))
for x in b:
    print("@"*x)"""
#A Python program that concatenates all elements in a list into a string and returns it.
""""a=int(input("Enter the size of list:"))
c=[]
for x in range(a):
    c.append(str(input("Enter the items: ")))
b=""
for x in c:
    b=b+" "+x
print(b.strip())"""
#convert int to string of list items
"""a=[1,2,3,4]
b=[]
for x in a:
    b.append(str(x))
print(b)"""
#a Python program to print all even numbers from a given list 
#of numbers in the same order and stop printing 
#any after 237 in the sequence. Sample numbers list :
"""n = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
a=[]
for x in n:
    if (x%2==0) and (x<237):
       a.append(x)
print(a)"""
#A Python program that prints out all colors from color_list_1 that are not present in color_list_2.
"""color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
result=color_list_1 - color_list_2
print(result)"""
#A Python program that will accept the base and height of a triangle and compute its area.
"""def area_triangle(a,b):
    c=1.0/2.0*a*b
    print(f"The area of triangle is {c:.2f}")
a=float(input("Enter the height of traingle: "))
b=float(input("Enter the base of traingle: "))
area_triangle(a,b)"""
#A Python program that computes the greatest common divisor (GCD) of two positive integers.
"""import math
def gcd(a,b):
    temp=0
    while b!=0:
       temp=b
       b=a%b
       a=temp
    return a
def l_cm(a,b):
    return (a*b)//gcd(a,b)#(/) returs float and (//) returns int
a=abs(int(input("Enter first number:")))
b=abs(int(input("Enter second number:")))
print(f"gcd is {gcd(a,b)}")
print(f"lcm is {l_cm(a,b)}")"""
#A Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a==b or a==c or b==c:
        sum=0
        print(f"The sum is {sum}")
else:print(f"The sum is {a+b+c}")"""
#A Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if 15<(a+b)<20:
    print(20)
else:print(a+b)"""
#A Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a==b or (a+b)==5 or (a-b)==5:
    print(True)
else:print(False)"""
#A Python program to add two objects if both objects are integers.
"""a=5
b=6
if (type(a)==int) and (type(b)==int):
    print(a+b)#(isintance)  is used to check if an object is an instance of a specific class or type in Python.
else:print(False)"""#syntax(isinstance(object,class))
#A Python program that displays your name, age, and address on three different lines.
"""a=str(input("Enter your name: "))
b=int(input("Enter your age: "))
c=str(input("Enter your address: "))
print(f"your name is    :{a}")
print(f"your age is     :{b}")
print(f"your address is :{c}")"""
#A Python program to solve (x + y) * (x + y).
"""x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
print((x + y) **2)"""
#A Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
"""a=int(input("Enter the amount: "))
t=int(input("Enter the year: "))
r=float(input("Enter the rate of interest: "))
n=1#Number of times interest is paid
ci=a*(1+(0.01*r))**t                                                           
print(f"The future value is:{ci:.2f}")"""
#A Python program to calculate the distance between the points (x1, y1) and (x2, y2)
"""import math as m
p1 = [4, 0]
p2 = [6, 6]
distance = m.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
print(distance)"""
#A Python program to check whether a file exists.
"""import os.path
print(os.path.isfile("prime.py"))"""
"""import site
print(site.getsitepackages())"""
#A Python program to find out the number of CPUs used.
"""import multiprocessing as m
count=m.cpu_count()
print(count)"""
#A Python program to print without a newline or space.
"""for i in range(0,10):
    print("*",end="")"""
#41-57 later
#A Python program to sum the first n positive integers.
"""import math
n=abs(int(input("Enter the n number: ")))
sum=0
for i in range(0,n+1):
    sum=sum+i
print(sum)"""
#A Python program to convert height (in feet and inches) to centimeters.
"""a=abs(float(input("Enter the size: ")))
b=input(""write inch if you want inches to centimeter: 
           write feet if you want feet to centimeter  :"").lower()
if b=="feet":
    print(f"the answer is = {a*30.48}cm ")
elif b=="inch":
    print(f"The answer is = {a*2.54}cm")
else: print("Choose from given option")"""
#A Python program to calculate the hypotenuse of a right angled triangle
"""import math
a=float(input("Enter the size of base: "))
b=float(input("Enter the size of height: "))
c=math.sqrt((a**2)+(b**2))
print(c)"""
#A Python program to convert the distance (in feet) to inches, yards, and miles.
"""import math
a=abs(float(input("Enter the distance in (feet): ")))
b=input("choose in which you want to convert(inches/yards,miles): ")
if b=="inches":
    print(a*12)
elif b=="yards":
    print(a*0.33)
elif b=="miles":
    print(f"{a*0.000189:.2f}")
else: print("choose from option")"""
#A Python program to convert all units of time into seconds.
"""a=float(input("Enter the value: "))
b=input("Enter the h if you  want hour to second : " \
        "Enter the m if you want minute to second: ")
if b=="h":
    print(a*60*60)
elif b=="m":
    print(a*60)
else: print("choose from option")"""
#A Python program to calculate the body mass index.
"""a=float(input("Enter your weight in kilogram: "))
b=float(input("Enter height in feet: "))
c=b*0.305
print(f"{a/c**2:.2f}")"""
#A Python program to calculate sum of digits of a number.
"""a=input("Enter a multi-digit number: ")
b=0
for x in a:
    c=int(x)
    b=b+c
print(b)"""
#A Python program to sort three integers without using conditional statements and loops.
"""a=int(input("Enter the a number: "))
b=int(input("Enter the a number: "))
c=int(input("Enter the a number: "))
a_min=min(a,b,c)
a_max=max(a,b,c)
a_mid=(a+b+c)-a_min-a_max
print(f"the max number = {a_max}")
print(f"The mid number = {a_mid}")
print(f"The min number = {a_min}")"""
#A Python program to calculate the midpoints of a line.
"""a=int(input("Enter the x coordinate of first end:"))
b=int(input("Enter the y coordinate of first end:"))
#inputing second end cordinates
c=int(input("Enter the x coordinate of second end:"))
d=int(input("Enter the y coordinate of second end:"))
x_mid=(a+b)/2
y_mid=(c+d)/2
print(f"the midpoint coordinates are ({x_mid,y_mid})")"""
#A Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
"""a=[1,2,3,4,7,2]#list
b=(1,2,3,4,5)#tuple
c={1,2,3,4,5}#set
g={"a":1,"b":2,"c":3,"d":4,"e":5}
h=0
f=0
d=0
e=0
for x in a:
    f=f+x
print(f)
for x in b:
    d=d+x
print(d)
for x in c:
    e=e+x
print(e)
for x in g.values():
    h+=x
print(h)"""
#A Python program to test whether all numbers in a list are greater than a certain number.
"""a=[7,5,9,7,8,5,76,4,766,8,4,7,56]
b=int(input("enter a number that you want to check: "))
for x in a:
    if b>=x:
        print(False)
        break
    else: print(True)
    break"""
#A Python program to count the number of occurrences of a specific character in a string.
"""a="alljfnalslajsflasc"
count=0
for x in a:
    if x=="a":
        count+=1#This logical but we can use count() function to count
print(count)
print(a.count("a"))"""#this will print the same
#A Python program to get the size of a file.
"""import os
print(os.path.getsize("list.py"))"""
#A Python program to get the Identity, Type, and Value of an object.
"""a=5
b="yo"
c=3.5
print(type(a))
print(type(b))
print(type(c))"""
#A Python program to convert the bytes in a given string to a list of integers
"""a=b"lol"
print(list(a))"""
#A Python program to find the sum of ASCII values of characters in a string.
"""a="ABC"
b=0
for x in a:
    b=b+(ord(x))
print(b)"""
#Dcitionary to list #by defualt it prints keys 
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
hmm=list(thisdict.values())
print(hmm)"""
#nested dictionary
"""child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child1"]["name"])"""
#Basic decorator
"""def dec(func):
    def greet(a,b):
        print("good morning")
        func(a,b)
        print("Bye Bye")
    return greet
@dec
def add(a,b):
    print(a+b)
add(4,5)"""
#a program to make double the item in the list
"""a=[1,2,3,4,5]
b=[]
for x in a:
    b.append(x*1)
print(b)"""
#open and read the file
"""f=open("hash.txt.txt","rt")
print(f.read())"""
"""f=open("C:\\timepass\\aisehi.txt","rt")
print(f.read())"""
#checking path exists or the size of file
"""import os
path=r"c:\timepass\aisehi.txt"
print(os.path.exists(path))
print(os.path.getsize(path))"""
#Revise
'''print("""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
      """)'''
#2
"""import sys
print(sys.version)"""
#4
"""r=int(input("Enter the radius: "))
print(f"the area of circle ={3.14*r*r}")"""
#5
"""f_name=input("Enter the first name: ")
l_name=input("Enter the last name : ")
print(l_name+" "+f_name)"""
#6
"""import random as rd
b=[]
a=int(input("Enter the size of list"))
for x in range(a):
    b.append(rd.randint(0,9))
print(b)"""
#7
"""f = input("Input the Filename: ")
x=f.split(".")
print(x[-1])"""
#8
"""color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])"""
#10
"""n=input("enter the value of n: ")
a=int(n)
b=int(n+n)
c=int(n+n+n)
print(f"The sum is {a+b+c}")"""
#Write a Python program to sum and multiply all the items in a list.
"""a=[1,26,8,4,3,7]
sum=0
multi=1
for x in a:
    sum+=x
    multi*=x
print(f"The sum is : {sum}")
print(f"The multiplication is : {multi}")"""
#Write a Python program to get the largest number from a list.
"""a=[1,26,8,4,3,7]
a.sort()
print(a[-1])"""# using sort function
#Basic manual sorting
"""a=[1,26,8,4,3,7]
b=a[0]
for x in a:
    if x>b:
        b=x
print(b)"""
#Write a Python program to get the smallest number from a list.
"""a=[11,26,8,4,3,7]
b=a[0]
for x in a:
    if x<b:
        b=x
print(b)"""
#By using sort function
"""a=[11,26,8,4,3,7]
a.sort() #By asending
print(a[0])
a.sort(reverse= True)# BY desending
print(a[-1])"""
#Write a Python program to count the number of strings from a 
#given list of strings. The string length is 
#2 or more and the first and last characters are the same.
"""a=['abc', 'xyz', 'aba', '1221']
count=0
for x in a:
    if len(x)>1 and x[0]==x[-1]:
        count+=1
print(count)"""
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
"""a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
b=sorted(a, key=lambda x: x[-1])
print(b)"""
#find the factorial
"""def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(3))"""
#find the fibbonacci at nth term
"""def fibbo(n):
    if n<=1:
        return n
    return fibbo(n-1)+fibbo(n-2)
print(fibbo(8))"""
#find the sum of list by recursion
"""def sum_l(n):
    if len(n)==0:
        return 0
    return n[0]+sum_l(n[1:])
a=[1,2,3,4,5]
print(sum_l(a))"""
#can manually set recusion to deeper recursion
"""import sys
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())"""
#generator
"""def mugen():
    yield 1
    yield 2
    yield 3
gen=mugen()
print(next(gen))
print(next(gen))
print(next(gen))"""
"""x=range(10)
print(list(x))"""
#try-except
"""try:
    f=open("text_p.txt","w")
    try:
        f.write("hello")
    except:
        print("Something is wrong when writing the file")
    finally:
        f.close()
except:
    print("Something is wrong while opening the file")"""

