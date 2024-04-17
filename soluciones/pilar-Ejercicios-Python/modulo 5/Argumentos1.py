#Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, 
#y que retorne la suma de sus valores al cuadrado.


#Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

import math


def suma_cuadrados(numeros):
    suma=0
    for i in range(len(numeros)): 
      suma+=math.pow(numeros[i],2)
    return suma
numeros=[2,3,4,5,5]
suma=suma_cuadrados(numeros)
print("la suma es: "+ str(suma))