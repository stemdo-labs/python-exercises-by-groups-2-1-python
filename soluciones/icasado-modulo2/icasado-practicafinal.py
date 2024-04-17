nombre = input("Introduzca un nombre: ")
monto = input("Introduzca un monto de ventas del mes: ")

comision = int(monto) / 100 * 13

print("Hola, " + nombre + ". Tu comision es: " + str(comision))

