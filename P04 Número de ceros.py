suma = 0
N = int(input('¿Cuantos números quieres decirme?'))
for i in range (1, N+1):
  cosa = int(input('dime número ' + str(i) + ': '))
  if (cosa == 0):
    suma = suma + 1
print('hay ' + str(suma) + ' ceros.')