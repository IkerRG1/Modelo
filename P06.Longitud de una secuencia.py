cantidad = 0
while True:
  n = int(input('Dime un número'))
  if n == 0:
    break
  cantidad += 1
print('El número de números introducidos es' +' '+ str(cantidad))