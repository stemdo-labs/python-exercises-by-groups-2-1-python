#Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

#Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() 
#de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
class Personaje:
    def atacar(self):
        pass

class Mago(Personaje):
    def atacar(self):
        print("Mago atacando")

class Arquero(Personaje):
    def atacar(self):
        print("Arquero atacando")

class Samurai(Personaje):
    def atacar(self):
        print("Samurai atacando")

personajes =[Mago(),Arquero(),Samurai()]

for personaje in personajes:
    personaje.atacar()