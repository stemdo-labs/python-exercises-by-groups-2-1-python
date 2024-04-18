import random
 
puntos_nuevos = int(random.randint(1,20))
puntos_totales = 12 + puntos_nuevos

puntos_nuevos = str(puntos_nuevos)
puntos_totales = str(puntos_totales)

print("Has ganado " + puntos_nuevos + " puntos! En total, acumulas " + puntos_totales + " puntos")