km1 = int(input('Dime los Km que puedes correr:'))
km2 = int(input('Dime los Km que tienes que correr:'))
while km1 < km2:
  i = int(km1) * 0.1
  km1 = km1+i
print(int(km1+1))