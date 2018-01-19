print('Dime dos números enteros')
A = int(input('Número 1:'))
B = int(input('Número 2:'))

if (A == B):
  print('No funcionará')
if (A > B):
  for i in range (B, A+1):
    print(i)
if (A < B):
  for i in range (A, B+1):
    print (i)