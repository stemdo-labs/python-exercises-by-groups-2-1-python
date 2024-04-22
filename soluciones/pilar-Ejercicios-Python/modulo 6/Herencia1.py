#Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

    
alumno1=Alumno("Pedro",19)

print("El alumno es: "+alumno1.nombre + " y tiene "+str(alumno1.edad)+" años")
