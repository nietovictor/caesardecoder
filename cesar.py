import time
import nltk
from nltk.corpus import cess_esp
# Verifica si el corpus ya está descargado
try:
    nltk.data.find('corpora/cess_esp.zip')
except LookupError:
    nltk.download('cess_esp', quiet=True)
spanish_words = set(cess_esp.words())

# Crea un array con todas las letras del alfabeto, incluyendo la ñ si asi se indica
alfabeto = [chr(i) for i in range(97, 123)]

n = input("¿Quieres incluir la ñ? si/no \n")
if n == "si":
    alfabeto.insert(alfabeto.index('n') + 1, 'ñ')

# Pregunta si quieres probar todos los posibles desplazamientos y pide la palabra a descifrar
probar = input("¿Quieres probar todos los posibles desplazamientos? si/no \n")
palabra = input("Introduce la palabra a descifrar: ")

# Si quieres probar todos los desplazamientos, se recorre un bucle para cada desplazamiento y se va imprimiendo cada palabra
if probar == "si":
    pruebas = ""
    palabra_correcta = ""
    indice_correcto = 0
    for i in range(1, 27):
        for letra in palabra:
            if letra in alfabeto:
                indice = alfabeto.index(letra)
                nuevo_indice = (indice + i) % len(alfabeto)
                pruebas += alfabeto[nuevo_indice] 
            else:
                pruebas += letra
        if pruebas in spanish_words:
            indice_correcto = i
            palabra_correcta = pruebas
        print(f"{i}. {pruebas}")
        time.sleep(0.25)
        pruebas = ""

    print("\n Parece que la palabra correcta es " + palabra_correcta + " con un desplazamiento de " + str(indice_correcto))
    
# Si quieres un desplazamiento especifico, se pide un numero y se imprime la palabra resultante con ese desplazamiento
if probar =="no":
    numero = int(input("Introduce el número de posiciones a desplazar: "))
    palabra_descifrada = ""
    for letra in palabra:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + numero) % len(alfabeto)
            palabra_descifrada += alfabeto[nuevo_indice] 
        else:
            palabra_descifrada += letra
    print("La palabra descifrada es: " + palabra_descifrada)



