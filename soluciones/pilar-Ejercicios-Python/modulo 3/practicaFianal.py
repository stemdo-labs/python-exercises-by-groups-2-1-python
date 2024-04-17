
##### En este ejercicio, crearás un programa en Python que solicita al usuario un texto y tres letras, y realiza varios análisis sobre el texto ingresado. El programa mostrará al usuario los resultados de estos análisis.

def countLettersIntext(texto, letras):
    datos = {}
    for i in range(len(letras)):
        numeroVecesRepetidas = texto.count(str(letras[i]))
        datos[letras[i]] = numeroVecesRepetidas
    return datos

def countWordsInText(texto):
    palabras=texto.split(' ')
    numWords=len(palabras)
    return numWords

def firstAndLast(texto):
    size=len(texto)
    first=str(texto[0])
    last=str(texto[size-1])
    return first,last

def reverseText(texto):
    palabras=texto.split(' ')
    palabraReversed=' '.join(palabras)[::-1]
    return palabraReversed

def isPython(texto):
    palabra="python"
    return texto.count(palabra)>0

texto = input("Introduce un texto: ")
letras = input("Introduce tres letras: ")

textToLower = texto.lower()
letrasToLower = letras.lower()
print("ANALISIS DEL TEXTO\n")
print("------------------------------------------------")
resultados = countLettersIntext(textToLower, letrasToLower)
print("Las letras que aparecen repetidas son:", resultados)
palabras=countWordsInText(textToLower)
print("el número de palabras son:", palabras)
first,last=firstAndLast(textToLower)
print("La primera palabra es: "+first +" y la última es: "+last)
reversed=reverseText(textToLower)
print("El texto con las palabras al reves: "+reversed)
exist=isPython(textToLower)
if(exist):
   print("La palabra Python existe en el texto")
else:
    print("La palabra Python NO existe en el texto")
print("------------------------------------------------")

