#La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.

#Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

palabra="pilar"
lista=["abrigo","calcetín","zapato"]
tupla=(1,2,3)
objects=[palabra, lista, tupla]
for i in range(len(objects)):
    print(len(objects[i]))