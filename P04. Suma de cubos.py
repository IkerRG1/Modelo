suma = 0

N = int(input('Dime un número: '))
for i in range (N+1):
  print(i)
  suma = suma + i**3
print(suma)