#Crea una función llamada numeros_persona que reciba, 
#como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
#La función debe devolver el siguiente mensaje:
#"{nombre}, la suma de tus números es {suma_numeros}"
def numeros_persona(nombre, numeros):
    suma = 0
    for i in range(len(numeros)):
        suma += numeros[i]
    print("Nombre " + nombre + " la suma de tus números es: " + str(suma))

numeros = [1, 2, 3]
nombre = "Pilar"
numeros_persona(nombre, numeros)
