suma = 0
multiplicacion = 1

N = int(input('Dime un número:'))
for i in range (1, N+1):
  print(i)
  multiplicacion = multiplicacion*i
  suma = suma + multiplicacion
print(suma)