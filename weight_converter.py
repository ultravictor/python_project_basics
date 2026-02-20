w=float(input("Enter the weight :"))
unit=input("""Enter the unit [(k) for kilogram :]
               [(p) for pounds   :]""").lower()
if unit=="k":
    a=w/2.205
    print(f"weight is {a} KG")
elif unit=="p":
    a=w*2.205
    print(f"weight is {a} POUND")
else: print("You didn't choose from given option ")
   