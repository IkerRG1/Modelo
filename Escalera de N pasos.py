N = int(input('Dime un número, menor o igual que nueve:'))

if (N <= 9):
  for i in range (1,N+1):
    for j in range (1, i+1):
      print(j, end='')
    print()

else:
  print('El número debe ser menor o igual que nueve.')