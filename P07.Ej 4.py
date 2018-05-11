#Esto es lo que hice yo
#def fibonacci(n):
  #f0 = 0
  #f1 = 1
  #fn = n
  #return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(5))

#Esto lo busque por google
#def fibonacci(n):
    #a, b = 0,1
    #while a < n:
        #print(a)
       # #a, b = b, (a+b)
    #print()



#Y esto tambien pero es casi igual a lo que tenia yo y lo entiendo.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input('Dime el número para saber a que número de la sucesión de fibonacci pertenece:'))

print(fib(n))