cantidad = 0
grande = 0
grande2 = 0
posicion = 0
posiciong = 0
posiciong2 = 0
while True:
  n = int(input('Dime un número:'))
  posicion += 1
  if n < grande:
    grande = grande
    if n < grande2:
      grande2 = grande2
    else:
      grande2 = n
      posiciong2 = posicion
  else:
    grande = n
    posiciong = posicion
  cantidad += 1
  if n == 0:
    break
print('La cantidad de números introducidos es' +' '+ str(cantidad-1))
print('El número más grande de la cadena es' +' '+ str(grande) +' y está en la posición' +' '+ str(posiciong))
print('El número más grande de la cadena es' +' '+ str(grande2) +' y está en la posición' +' '+ str(posiciong2))