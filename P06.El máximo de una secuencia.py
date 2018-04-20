cantidad = 0
grande = 0
while True:
  cantidad += 1
  n = int(input('Dime un número:'))
  if n < grande:
    grande = grande
  else:
    grande = n
  if n == 0:
    break
print('El número de números introducidos es' +' '+ str(cantidad-1))
print('El número más grande de la cadena es' +' '+ str(grande))