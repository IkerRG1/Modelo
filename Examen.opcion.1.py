cadena = input('Dime una cadena con 2 t como minimo:')
print(cadena)
t1 = (cadena.find('t'))
print('primera t esta en' + ' ' + str(t1))
t2 = (cadena.rfind('t'))
print('última t esta en' + ' ' + str(t2))
print((cadena[:t1]) + (cadena[t2+1:]))