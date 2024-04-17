##### Tu amigo ha creado una fábrica de cerveza y necesita darle a su producto una identidad única. Diseña un programa en Python que solicite al usuario ingresar dos palabras, y luego combine esas palabras para formar un nombre creativo para la cerveza. Asegúrate de que el nombre de la cerveza se muestre entre comillas en dos líneas separadas para resaltar su singularidad. Este ejercicio evaluará tu capacidad para utilizar variables, entrada de usuario, concatenación de cadenas y salida de datos en Python.+

# Pedir al usuario que ingrese dos palabras
palabra1 = input("Por favor, ingresa una palabra: ")
palabra2 = input("Ahora, ingresa otra palabra: ")

# Combinar las palabras para formar el nombre de la cerveza
nombre_cerveza = palabra1 + " " + palabra2

# Mostrar el nombre de la cerveza entre comillas en dos líneas
print("\nEl nombre de tu cerveza creativa es:")
print('"' + nombre_cerveza + '"')