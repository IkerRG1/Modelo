km1 = int(input('Dime los Km que puedes correr:'))
km2 = int(input('Dime los Km que tienes que correr:'))
dias = 0
while km1 < km2:
  i = int(km1) * 0.1
  km1 = km1+i
  dias += 1
print("al" + str(dias) + " dia corro"+str(int(km1+1)) + ' ' + 'km')