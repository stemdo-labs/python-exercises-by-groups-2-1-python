text = input("Ingresa un texto: ")
letras = input("Ingresa tres letras: ")

# Borrar espacios en blanco por si acaso se introducen en el input de las letras
list_letras = list(letras.replace(" ", ""))

for l in list_letras:
    print("Letra " + l + ": " + str(text.count(l)))
