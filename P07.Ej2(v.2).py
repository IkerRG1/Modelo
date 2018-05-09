
def potencia(x,n):
  resultado=0
  exp=1
  if n == 0:
      return 1
  for i in range(1,n+1):
    exp = exp*x
   # resultado = resultado + (n*exp)
    
   # return resultado
  return exp
    

print(potencia(5,5)) 