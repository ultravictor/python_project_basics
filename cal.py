def add(a,b):
    return print(a+b)
def sub(a,b):
    return print(a-b)
def multi(a,b):
    return print(a*b)
def div(a,b):
    return print(a/b)
a=float(input("Enter your first number         :"))
b=float(input("Enter your second number        :"))
c=input("Enetr the opetaion you want (+,-,x,/) :")
match c:
    case "+":
        add(a,b)
    case "-":
        sub(a,b)
    case "x":
        multi(a,b)
    case "/":
        div(a,b)
    case _:
        print("You didn't choose from given operation (+,-,x,/)")
