cantidad = 0
grande = 0
posicion = 0
posiciong = 0
#1
while True:
  n = int(input('Dime un número:'))
  #2
  posicion += 1
  #1
  if n < grande:
    grande = grande
  else:
    grande = n
    posiciong = posicion
  #2
  cantidad += 1
  #1
  if n == 0:
    break
print('La cantidad de números introducidos es' +' '+ str(cantidad-1))
print('El número más grande de la cadena es' +' '+ str(grande) +' y está en la posición' +' '+ str(posiciong))
#2