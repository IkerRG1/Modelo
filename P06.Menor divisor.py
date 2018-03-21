n = int(input('Dime un número mayor que 2:'))
d = 2
while True:
  if n/d == n//d:
    print(str(d) + ' ' + 'es el menor divisor')
    break
  d+=1