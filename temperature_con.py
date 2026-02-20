temp=float(input("Enter the temperature :"))
unit=input("""Enter the unit [(c) for celcius       :]
               [(f) for farenheight   :]""").lower()
if unit=="c":
    a=(temp-32)/1.8
    print(f"The temperatureis {a} celcius")
elif unit=="f":
    a=(temp*1.8)+32
    print(f"The temperatureis {a} farenheight")
else: print("You didn't choose from given option")
