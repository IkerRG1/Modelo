año = int(input('¿Qué año?'))
if (año % 4 == 0) and (año % 100 != 0):
    print('bisiesto')
elif (año % 400 == 0):
    print('bisiesto')
else:
    print('no bisiesto')