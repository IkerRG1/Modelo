import math


def d(x1,x2,y1,y2):
  resultado=math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return resultado

x1 = int(input('Define x en el punto 1:'))
y1 = int(input('Define y en el punto 1:'))

x2 = int(input('Define x en el punto 2:'))
y2 = int(input('Define y en el punto 2:'))

print(d(x1,x2,y1,y2))