inicioX = int(input('Casilla de inicio X'))
inicioY = int(input('Casilla de inicio Y'))
finalX = int(input('Casilla de final X'))
finalY = int(input('Casilla de final Y'))


#pares = (inicioX % 2 == 0) and (inicioY % 2 == 0) and (finalX % 2 == 0) and (finalY % 2 == 0)
#impares = (inicioX % 2 != 0) and (inicioY % 2 != 0) and (finalX % 2 != 0) and (finalY % 2 != 0)
#
#
#if (inicioX + inicioY == pares):
#     print('casilla negra')
#
#elif (inicioX + inicioY == impares):
#     print('casilla blanca')

if((inicioX > 8) or (inicioY > 8) or (finalX > 8) or (finalY > 8)) or ((inicioX < 0) or (inicioY < 0) or (finalX < 0) or (finalY < 0)):
    print('No es válido para el tablero de ajedrez')
elif((inicioX + inicioY)%2 == 0): #la primera es negra
    if((finalX + finalY)%2 == 0): #la segunda es negra
        #inicio es negra y final es negra
        print('inicio y final son negras')
    if((finalX + finalY)%2 != 0): #la segunda es blanca
        #inicio es negra y final es blanca
        print('inicio es negra y final es blanca')

elif((inicioX + inicioY)%2 != 0): #la primera es blanca
    if((finalX + finalY)%2 != 0): #la segunda es blanca
        #inicio es blanca y final es blanca
        print('inicio es blanca y final es blanca') 
    if((finalX + finalY)%2 == 0): #la segunda es negra
        print('inicio es blanca y final es negra')
   