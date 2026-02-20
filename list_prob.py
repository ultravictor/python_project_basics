a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""if len(a)>len(b):
    c=[x for x in b if x in a]
elif len(a)==len(b):
    c=[x for x in b if x in a]
else: c=[x for x in a if x in b]
d=set(c)
print(d)"""
print(list(set(a) & set(b)))# this the code for print a list that is common in two list without duplicte and in one line
