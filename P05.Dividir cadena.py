s = str(input('Escribe una frase:'))
print(len(s))
print(s[:(len(s)//2)])
print(s[(len(s)//2):])

print(str(s[(len(s)//2):]) + str(s[:(len(s)//2)]))