x = input('numero 1 = ')
z = input('numero 2 = ')
y = input('numero 3 = ')
if (x < z) and (x < y):
    print (x)
elif (y < x) and (y < z):
    print (y)
else:
    print (z)