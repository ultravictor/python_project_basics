a="My name is Michele"
b=a.split(" ")
z=""
for x in b[::-1]:
    z=z+" "+x
print(z.strip())