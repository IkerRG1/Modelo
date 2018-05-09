
def potencia(x,n):
  #resultado=0 para for
  #exp=1 para for
  if n == 0:
      return 1
  return x * potencia(x,(n-1))
print(potencia(4,3))    
  