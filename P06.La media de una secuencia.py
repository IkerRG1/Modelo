cantidad = 0
suma = 0
media = 1
while True:
  cantidad += 1
  n = int(input('Dime un número:'))
  suma = suma + n
  if n == 0:
    break
print('El número de números introducidos es' +' '+ str(cantidad-1))
print('La suma de todos los números introducidos son'+' '+str(suma))
media = suma/(cantidad-1)
print('La media de la secuencia es' +' '+ str(media))