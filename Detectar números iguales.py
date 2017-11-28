x = int(input('numero 1 = '))
y = int(input('numero 2 = '))
z = int(input('numero 3 = '))
if (x == y == z):
    print('3')
elif (x == y != z) or (x != y == z) or (x == z != y):
    print('2')
else:
    print('0')