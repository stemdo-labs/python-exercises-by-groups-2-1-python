##### En esta prueba, crearás un programa en Python para ayudar a calcular las comisiones de los vendedores de una empresa. El programa solicitará al usuario que ingrese su nombre y el monto de ventas que ha realizado en el mes. Luego, calculará la comisión del 13% sobre el monto de ventas ingresado y mostrará un mensaje que incluye el nombre del vendedor y el monto de la comisión.


clientName=input("Introduce tu nombre")
monto= float(input("Introdice el monto de ventas"))
comision=monto*0.13
print ("CLIENTE:"+clientName.upper())
print("------------------------------------------------")
print("Nombre_Cliente: "+str(clientName)+"\nMonto de ventas: "+str(monto)+"\nComision calculada: "+str(comision))
print("------------------------------------------------")
