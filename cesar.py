import time

# Crea un array con todas las letras del alfabeto, incluyendo la ñ si asi se indica
alfabeto = [chr(i) for i in range(97, 123)]
n = input("¿Quieres incluir la ñ? si/no \n")
if n == "si":
    alfabeto.insert(alfabeto.index('n') + 1, 'ñ')

# Pregunta si quieres realizar todos los posibles desplazamientos y pide la palabra a descifrar
palabra = input("Introduce la palabra a cifrar/descifrar: ")
desplazamientos = input("¿Quieres hacer todos los posibles desplazamientos? si/no \n")

# Si quieres realizar todos los desplazamientos, se recorre un bucle para cada desplazamiento y se va imprimiendo cada palabra
if desplazamientos == "si":
    palabras = ""
    for i in range(1, 27):
        for letra in palabra:
            if letra in alfabeto:
                indice = alfabeto.index(letra)
                nuevo_indice = (indice + i) % len(alfabeto)
                palabras += alfabeto[nuevo_indice] 
            else:
                palabras += letra
        print(f"{i}. {palabras}")
        time.sleep(0.25)
        palabras = ""
    
# Si quieres un desplazamiento especifico, se pide un numero y se imprime la palabra resultante con ese desplazamiento
if desplazamientos =="no":
    numero = int(input("Introduce el número de posiciones a desplazar: "))
    palabra_descifrada = ""
    for letra in palabra:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + numero) % len(alfabeto)
            palabra_descifrada += alfabeto[nuevo_indice] 
        else:
            palabra_descifrada += letra
    print("La palabra cifrada/descifrada es: " + palabra_descifrada)