#Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
class Mascota():
    @staticmethod
    def respirar():
       return print("inhalar....Exhalar")
    
mascota1=Mascota()
mascota1.respirar()