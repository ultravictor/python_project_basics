while True:
    p=float(input("Enter the principal amount : "))
    if p<=0:
        print("Principal can't be zero or negative ")
        break
    t=float(input("Enter the time : "))
    if t<=0:
        print("Time can't be zero or negative ")
        break
    r=float(input("Enter the rate of interest : "))
    if r<=0:
        print("Rate of Interest can't be zero or negative ")
        break
    total=p*(1+r/100)**t
    print(f"The final amount will be = {total:.2f}")
    break