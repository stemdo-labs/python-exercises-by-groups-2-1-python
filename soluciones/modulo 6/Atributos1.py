#Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

#Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca=Casa("blanco",4)
print("El color es: "+casa_blanca.color)
print("El número de pisos es: "+str(casa_blanca.cantidad_pisos))