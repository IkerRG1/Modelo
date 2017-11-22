inicioX = int(input())
inicioY = int(input())
finalX= int(input())
finalY = int(input())
if (inicioX != finalX) and (inicioY != finalY):
    print('No')
elif (inicioX == finalX) or (inicioY == finalY):
    print('Yes')