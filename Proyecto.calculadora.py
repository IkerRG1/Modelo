#Esto es una calculadora

#Operaciones: 
#-Factorial
#-Potencia
#-Sumar Factoriales
#-Sumar Cubos

#Esta es la función para hacer el Factorial.
def factorial(j):
  if j == 0:
    return 1
  else:
    return j*factorial(j-1)
#Aquí acaba la función factorial    

#Esta es la función para hacer la Potencia.
def potencia(x,n):
  if n == 0:
      return 1
  return x * potencia(x,(n-1))
#Aquí acaba la función potencia

#Esta es la función para Sumar Factoriales.
def sfactoriales(n):
  suma = 0
  multiplicacion = 1
  #n = int(input())
  for i in range (1, n+1):
    multiplicacion = multiplicacion*i
    suma = suma + multiplicacion
  return suma
#Aquí acaba la función Sumar Factoriales.

#Esta es la función sumar cubos.
def scubos(k):
  suma = 0
  for i in range(1,k+1):
    suma = suma + i**3
  return suma
#acaba función scubos


while True:
  #Aquí voy a hacer el menú para la calculadora.
  print('Elije la operación que quieras calcular:')
  print('Press 1 for factorial', sep = '  ')
  print('Press 2 for potencia' , sep = '  ')
  print('Press 3 for sumar factoriales' , sep = '  ')
  print('Press 4 for Sumar Cubos' , sep = '  ')
  print('Press 0 to exit' , sep = '  ')

  obj = int(input())
  #Esta es la parte del menu que elije el factorial
  if obj == 1:
    print('Elije el factorial que quieras calcular.')
    num = int(input())
    print(factorial(num))
    
  #esta es la parte del menu que realiza una potencia
  if obj == 2:
    print('Elije la base y el exponente que quieras calcular.')
    bas = int(input())
    exp = int(input())
    print(potencia(bas,exp))
  
  #esto realizará la suma de los factoriales
  if obj == 3:
    print('Elije el factorial que quieras sumar hacia atrás.')
    fact = int(input())
    print(sfactoriales(fact))
  
  #Esta es la función de sumar cubos
  if obj == 4:
    print('Elije un número para sumarlo elevado al cubo hasta llegar a 0.')
    p = int(input())
    print(scubos(p))



  #Esto es para finalizar el programa
  if obj == 0:
    break