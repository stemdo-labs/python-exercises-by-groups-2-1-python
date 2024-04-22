import random

nombre = input("Inserte un nombre: ")
n_secreto = random.randint(1,100)
# print(n_secreto)

print("He pensado un numero secreto. Tienes 8 intentos para adivinarlo")
count = 8

while count > 0 :
    num = input("Escribe un numero: ")
    if int(num) != n_secreto:
        count -= 1
        print("Ese no es el número. Te quedan " + str(count) + " intentos" )
    elif int(num) == n_secreto:
        print("Has acertado el número")
        break