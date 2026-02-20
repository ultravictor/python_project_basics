a=[]
b=[]
while True:
    x=input("Enter the food (q to quit)   :")
    if x.lower()=="q":
        break
    a.append(x)
    y=float(input(f"Enter the price of {x} :"))
    b.append(y)
print("----------FOODS IN CART--------------")
for i in range(len(a)):
    print(f"{a[i]}            {b[i]}")
total=0
for i in b:
    total+=i
print(f"The total amount is ======{total:.2f}RS")
