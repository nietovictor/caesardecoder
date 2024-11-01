import time
from pyrae import dle

print("Bienvenido a Caesar Decoder")
print("hecho por nietovictor and dawfunes")
time.sleep(0.5)

# Antes de nada, debemos seleccionar si queremos hacer con una rotación o cada cuantas letras.
# print("Antes de nada, debemos seleccionar si queremos hacer con una rotación o cada cuantas letras.")
# alternante = input("¿Quieres que se aplique el decodificado a todas las letras? si/no")
# if alternante == "no":
#     cada_cuantas_letras = input("Cada cuantas letras quieres que se aplique el codigo?")

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
    check_RAE = input("¿Quieres que saque las posibles soluciones al final (solo hacer con acceso a internet)? si/no")
    palabras_diccionario = []

    def check_word_in_rae(word, id):
        response = dle.search_by_word(word=word).to_dict()
        if response["title"] != "Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE":
            print("SI, puede ser nuestra solución")
            palabras_diccionario.append([word,id])
        else:
            print("NO, no puede ser nuestra solución")

    for i in range(1, 27):
        palabra_descifrada = ""
        for letra in palabra:
            if letra in alfabeto:
                indice = alfabeto.index(letra)
                nuevo_indice = (indice + i) % len(alfabeto)
                palabra_descifrada += alfabeto[nuevo_indice]
            else:
                palabra_descifrada += letra
        print(f"{i}. {palabra_descifrada}")
        if check_RAE == "si":
            check_word_in_rae(palabra_descifrada, i)

    for palabra in palabras_diccionario:
        print(f"\n{palabra[0]} es posiblemente la respuesta con {palabra[1]} rotaciones")
    
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